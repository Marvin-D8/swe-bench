import json
import os
import ast
import jedi
import shutil
import traceback
import subprocess
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List, Tuple, Set, Optional, Callable

from argparse import ArgumentParser
from datasets import load_from_disk, load_dataset
from filelock import FileLock
from git import Repo
from pyserini.search.lucene import LuceneSearcher
from tqdm.auto import tqdm

from swebench.inference.make_datasets.utils import list_files, string_to_bool

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


class ContextManager:
    """A context manager for managing a Git repository at a specific commit."""

    def __init__(self, repo_path: str, base_commit: str, verbose: bool = False):
        self.repo_path = Path(repo_path).resolve().as_posix()
        self.base_commit = base_commit
        self.verbose = verbose
        self.repo = Repo(self.repo_path)

    def __enter__(self):
        if self.verbose:
            print(f"Switching to {self.base_commit}")
        try:
            self.repo.git.reset("--hard", self.base_commit)
            self.repo.git.clean("-fdxq")
        except Exception as e:
            logger.error(f"Failed to switch to {self.base_commit}: {e}")
            raise
        return self

    def get_readme_files(self) -> List[str]:
        """Returns a list of README filenames in the repository root."""
        files = [
            f
            for f in os.listdir(self.repo_path)
            if os.path.isfile(os.path.join(self.repo_path, f))
            and f.lower().startswith("readme")
        ]
        return files

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def file_name_and_contents(filename: str, relative_path: str) -> str:
    """Encode document as filename + full file contents."""
    with open(filename, encoding="utf-8", errors="ignore") as f:
        return f"{relative_path}\n{f.read()}"


def file_name_and_documentation(filename: str, relative_path: str) -> str:
    """Encode document as filename + extracted docstrings."""
    text = f"{relative_path}\n"
    try:
        with open(filename, encoding="utf-8", errors="ignore") as f:
            source = f.read()
        node = ast.parse(source)
        module_doc = ast.get_docstring(node)
        if module_doc:
            text += module_doc
        for child_node in ast.walk(node):
            if isinstance(
                child_node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
            ):
                doc = ast.get_docstring(child_node)
                if doc:
                    text += f"\n\n{child_node.name}\n{doc}"
    except Exception as e:
        logger.error(f"Failed to parse file {filename}: {e}. Using full content.")
        return file_name_and_contents(filename, relative_path)
    return text


def file_name_and_docs_jedi(filename: str, relative_path: str) -> str:
    """Encode document as filename + jedi-extracted documentation."""
    text = f"{relative_path}\n"
    try:
        with open(filename, encoding="utf-8", errors="ignore") as f:
            source_code = f.read()
        script = jedi.Script(source_code, path=filename)
        module = script.get_context()
        text += f"{module.full_name}\n"
        if module.docstring():
            text += f"{module.docstring()}\n\n"
        names = [
            name
            for name in script.get_names(
                all_scopes=True, definitions=True, references=False
            )
            if not name.in_builtin_module()
        ]
        for name in names:
            try:
                origin = name.goto(follow_imports=True)[0]
                if (
                    origin.module_name != module.full_name
                    or name.parent().full_name != module.full_name
                ):
                    if name.type in {"statement", "param"}:
                        continue
                text += f"{name.full_name}\n"
                if name.docstring():
                    text += f"{name.docstring()}\n\n"
            except Exception:
                continue
    except Exception as e:
        logger.error(f"Failed to parse file {filename}: {e}. Using full content.")
        return file_name_and_contents(filename, relative_path)
    return text


DOCUMENT_ENCODING_FUNCTIONS = {
    "file_name_and_contents": file_name_and_contents,
    "file_name_and_documentation": file_name_and_documentation,
    "file_name_and_docs_jedi": file_name_and_docs_jedi,
}


def clone_repo(repo: str, root_dir: str, token: str) -> Path:
    """Clones a GitHub repository to a specified directory."""
    repo_dir = Path(root_dir) / f"repo__{repo.replace('/', '__')}"
    if not repo_dir.exists():
        repo_url = f"https://{token}@github.com/{repo}.git"
        logger.info(f"Cloning {repo} (PID: {os.getpid()})")
        Repo.clone_from(repo_url, repo_dir)
    return repo_dir


def build_documents(
    repo_dir: str, commit: str, document_encoding_func: Callable[[str, str], str]
) -> Dict[str, str]:
    """Builds a dictionary of documents from a repository at a specific commit."""
    documents = {}
    with ContextManager(repo_dir, commit):
        filenames = list_files(repo_dir, include_tests=False)
        for relative_path in filenames:
            filename = os.path.join(repo_dir, relative_path)
            documents[relative_path] = document_encoding_func(filename, relative_path)
    return documents


def make_index(
    repo_dir: str,
    root_dir: str,
    commit: str,
    document_encoding_func: Callable[[str, str], str],
    python: str,
    instance_id: str,
) -> Path:
    """Builds a Pyserini index for documents."""
    index_path = Path(root_dir) / f"index__{instance_id}" / "index"
    if index_path.exists():
        return index_path
    documents_path = Path(root_dir) / instance_id / "documents.jsonl"
    documents_path.parent.mkdir(parents=True, exist_ok=True)
    documents = build_documents(repo_dir, commit, document_encoding_func)
    with open(documents_path, "w", encoding="utf-8") as docfile:
        for relative_path, contents in documents.items():
            json.dump({"id": relative_path, "contents": contents}, docfile)
            docfile.write("\n")
    cmd = [
        python,
        "-m",
        "pyserini.index",
        "--collection",
        "JsonCollection",
        "--generator",
        "DefaultLuceneDocumentGenerator",
        "--threads",
        "2",
        "--input",
        str(documents_path.parent),
        "--index",
        str(index_path),
        "--storePositions",
        "--storeDocvectors",
        "--storeRaw",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        thread_prefix = f"(pid {os.getpid()}) "
        logger.error(f"Failed to build index for {instance_id}: {e.stderr}")
        raise Exception(f"{thread_prefix}Failed to build index for {instance_id}")
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    return index_path


def get_remaining_instances(instances: List[Dict], output_file: Path) -> List[Dict]:
    """Filters instances to exclude those already processed."""
    if not output_file.exists():
        output_file.parent.mkdir(parents=True, exist_ok=True)
        return instances
    processed_ids = set()
    with FileLock(str(output_file) + ".lock"):
        with open(output_file, encoding="utf-8") as f:
            for line in f:
                instance = json.loads(line)
                processed_ids.add(instance["instance_id"])
    logger.warning(f"Found {len(processed_ids)} existing instances. Will skip them.")
    return [inst for inst in instances if inst["instance_id"] not in processed_ids]


def search(instance: Dict, index_path: Path) -> Optional[Dict]:
    """Searches for relevant documents in the index."""
    instance_id = instance["instance_id"]
    try:
        searcher = LuceneSearcher(str(index_path))
        query_text = instance["problem_statement"]
        cutoff = len(query_text)
        while True:
            try:
                hits = searcher.search(query_text[:cutoff], k=20, remove_dups=True)
                break
            except Exception as e:
                if "maxClauseCount" in str(e) and cutoff > 100:
                    cutoff = int(cutoff * 0.8)
                    continue
                raise
        return {
            "instance_id": instance_id,
            "hits": [{"docid": hit.docid, "score": hit.score} for hit in hits],
        }
    except Exception as e:
        logger.error(f"Failed to process {instance_id}: {e}")
        return None


def search_indexes(
    instances: List[Dict], output_file: Path, index_paths: Dict[str, Path]
):
    """Searches indexes and writes results to output file."""
    for instance in tqdm(instances, desc="Retrieving"):
        instance_id = instance["instance_id"]
        if instance_id not in index_paths:
            continue
        results = search(instance, index_paths[instance_id])
        if results is None:
            continue
        with FileLock(str(output_file) + ".lock"):
            with open(output_file, "a", encoding="utf-8") as outfile:
                json.dump(results, outfile)
                outfile.write("\n")


def get_missing_ids(instances: List[Dict], output_file: Path) -> Set[str]:
    """Returns set of instance IDs that are missing from output file."""
    written_ids = set()
    if output_file.exists():
        with open(output_file, encoding="utf-8") as f:
            for line in f:
                instance = json.loads(line)
                written_ids.add(instance["instance_id"])
    all_ids = {inst["instance_id"] for inst in instances}
    return all_ids - written_ids


def get_index_paths_worker(
    instance: Dict,
    root_dir_name: str,
    document_encoding_func: Callable[[str, str], str],
    python: str,
    token: str,
) -> Tuple[str, Optional[Path]]:
    """Worker function to build index for a single instance."""
    repo = instance["repo"]
    commit = instance["base_commit"]
    instance_id = instance["instance_id"]
    try:
        repo_dir = clone_repo(repo, root_dir_name, token)
        index_path = make_index(
            repo_dir=repo_dir,
            root_dir=root_dir_name,
            commit=commit,
            document_encoding_func=document_encoding_func,
            python=python,
            instance_id=instance_id,
        )
        return instance_id, index_path
    except Exception as e:
        logger.error(f"Failed to process {repo}/{commit} (instance {instance_id}): {e}")
        return instance_id, None


def process_repo_instances(args: Tuple) -> List[Tuple[str, Optional[Path]]]:
    """Process all instances for a single repository sequentially."""
    repo_instances, root_dir_name, document_encoding_func, python, token = args
    return [
        get_index_paths_worker(
            instance, root_dir_name, document_encoding_func, python, token
        )
        for instance in repo_instances
    ]


def get_index_paths(
    remaining_instances: List[Dict[str, Any]],
    root_dir_name: str,
    document_encoding_func: Callable[[str, str], str],
    python: str,
    token: str,
    output_file: str,
    num_workers: int = 4,
) -> Dict[str, Path]:
    """
    Retrieves index paths using multiple processes.
    Instances from the same repository are processed sequentially to avoid git conflicts.
    """
    repo_to_instances = defaultdict(list)
    for instance in remaining_instances:
        repo_to_instances[instance["repo"]].append(instance)
    all_index_paths = {}
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        repo_args = [
            (instances, root_dir_name, document_encoding_func, python, token)
            for instances in repo_to_instances.values()
        ]
        future_to_repo = {
            executor.submit(process_repo_instances, args): repo
            for args, repo in zip(repo_args, repo_to_instances.keys())
        }
        total_instances = len(remaining_instances)
        with tqdm(total=total_instances, desc="Indexing") as pbar:
            for future in as_completed(future_to_repo):
                repo = future_to_repo[future]
                try:
                    repo_results = future.result()
                    for instance_id, index_path in repo_results:
                        if index_path is not None:
                            all_index_paths[instance_id] = index_path
                        pbar.update(1)
                except Exception as exc:
                    logger.error(f"Repository {repo} failed: {exc}")
                    pbar.update(len(repo_to_instances[repo]))
    return all_index_paths


def get_root_dir(
    dataset_name: str, output_dir: str, document_encoding_style: str
) -> Tuple[Path, Path]:
    """Creates and returns root directory for indexes."""
    root_dir = Path(output_dir) / dataset_name / f"{document_encoding_style}_indexes"
    root_dir.mkdir(parents=True, exist_ok=True)
    return root_dir, root_dir


def cleanup_directories(root_dir: Path, leave_indexes: bool = True):
    """Clean up temporary directories."""
    del_patterns = ["repo__*"]
    if not leave_indexes:
        del_patterns.append("index__*")

    for pattern in del_patterns:
        for dirname in root_dir.glob(pattern):
            shutil.rmtree(dirname, ignore_errors=True)


def main(
    dataset_name_or_path: str,
    document_encoding_style: str,
    output_dir: str,
    shard_id: Optional[int] = None,
    num_shards: int = 20,
    splits: Optional[List[str]] = None,
    leave_indexes: bool = True,
):
    """Main function to run BM25 retrieval."""
    if splits is None:
        splits = ["train", "test"]

    document_encoding_func = DOCUMENT_ENCODING_FUNCTIONS[document_encoding_style]
    token = os.environ.get("GITHUB_TOKEN", "git")
    if Path(dataset_name_or_path).exists():
        dataset = load_from_disk(dataset_name_or_path)
        dataset_name = os.path.basename(dataset_name_or_path)
    else:
        dataset = load_dataset(dataset_name_or_path)
        dataset_name = dataset_name_or_path.replace("/", "__")
    if shard_id is not None:
        for split in splits:
            dataset[split] = dataset[split].shard(num_shards, shard_id)
    if not set(splits).issubset(set(dataset.keys())):
        raise ValueError(f"Unknown splits: {set(splits) - set(dataset.keys())}")
    instances = []
    for split in splits:
        instances.extend(list(dataset[split]))
    python = subprocess.run(
        "which python", shell=True, capture_output=True, text=True
    ).stdout.strip()
    output_file = (
        Path(output_dir) / dataset_name / f"{document_encoding_style}.retrieval.jsonl"
    )
    remaining_instances = get_remaining_instances(instances, output_file)
    root_dir, root_dir_name = get_root_dir(
        dataset_name, output_dir, document_encoding_style
    )
    try:
        all_index_paths = get_index_paths(
            remaining_instances,
            root_dir_name,
            document_encoding_func,
            python,
            token,
            str(output_file),
        )
        logger.info(f"Finished indexing {len(all_index_paths)} instances")
        search_indexes(remaining_instances, output_file, all_index_paths)
        missing_ids = get_missing_ids(instances, output_file)
        logger.warning(f"Missing indexes for {len(missing_ids)} instances.")
        logger.info(f"Saved retrieval results to {output_file}")
    except KeyboardInterrupt:
        logger.info("Process interrupted by user")
    finally:
        logger.info(f"Cleaning up {root_dir}")
        cleanup_directories(root_dir, leave_indexes)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--dataset_name_or_path",
        type=str,
        default="SWE-bench/SWE-bench",
        help="Dataset to use for test set from HuggingFace Datasets or path to a save_to_disk directory.",
    )
    parser.add_argument(
        "--document_encoding_style",
        choices=DOCUMENT_ENCODING_FUNCTIONS.keys(),
        default="file_name_and_contents",
    )
    parser.add_argument("--output_dir", default="./retrieval_results")
    parser.add_argument("--splits", nargs="+", default=["train", "test"])
    parser.add_argument("--shard_id", type=int)
    parser.add_argument("--num_shards", type=int, default=20)
    parser.add_argument("--leave_indexes", type=string_to_bool, default=True)
    args = parser.parse_args()
    main(**vars(args))
