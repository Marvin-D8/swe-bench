import sqlite3
import importlib.resources as resources
import swebench.resources
from functools import cache
from swebench.utils import generate_heredoc_delimiter
from swebench.image_builder.dockerfile_gen._swebench.constants import (
    MAP_REPO_TO_ENV_YML_PATHS,
    MAP_REPO_TO_INSTALL,
    MAP_REPO_TO_REQS_PATHS,
    MAP_REPO_VERSION_TO_SPECS,
    SWE_BENCH_URL_RAW,
    _DOCKERFILE_BASE,
    HEADERS,
    REPLACE_REQ_PACKAGES,
    REPO_BASE_COMMIT_BRANCH,
)
from swebench.image_builder.constants import CONTAINER_ENV_NAME, CONTAINER_WORKDIR
from swebench.harness.constants import (
    NON_TEST_EXTS,
    START_TEST_OUTPUT,
    END_TEST_OUTPUT,
)
from swebench.utils import get_modified_files
import posixpath
import requests
import re
import os


@cache
def get_environment_yml_by_commit(repo: str, commit: str) -> str:
    for req_path in MAP_REPO_TO_ENV_YML_PATHS[repo]:
        reqs_url = posixpath.join(SWE_BENCH_URL_RAW, repo, commit, req_path)
        reqs = requests.get(reqs_url, headers=HEADERS)
        if reqs.status_code == 200:
            break
    else:
        raise ValueError(
            f"Could not find environment.yml at paths {MAP_REPO_TO_ENV_YML_PATHS[repo]} for repo {repo} at commit {commit}"
        )

    lines = reqs.text.split("\n")
    cleaned = []
    for line in lines:
        # Rename environment to given name
        if line.startswith("name:"):
            cleaned.append(f"name: {CONTAINER_ENV_NAME}")
            continue
        cleaned.append(line)

    return "\n".join(cleaned)


def clean_environment_yml(yml_text: str) -> str:
    """
    Clean environment.yml by removing packages that have been yanked from PyPI

    conda style yamls take the form:
    ...
    - channels:
        ...
    - dependencies:
        ...
    - pip:
        - pkg_to_replace
        - pkg_to_replace
    - ... (more dependencies)

    We want to replace packages in the pip section only.
    """
    pip_match = re.search(r"^(\s*-\s*pip\s*:\s*\n)", yml_text, flags=re.MULTILINE)
    if not pip_match:
        return yml_text
    pip_line_start = pip_match.start()
    # get indentation level of pip line
    pip_indent = len(pip_match.group(1)) - len(pip_match.group(1).lstrip())
    pip_content_start = pip_match.end()
    # find where pip section ends by looking for a line that's at same or less indentation
    # or a line that starts a new top-level dependency (not pip)
    lines_after_pip = yml_text[pip_content_start:].split("\n")
    pip_section_end = pip_content_start
    for ix, line in enumerate(lines_after_pip):
        if line.strip() == "":
            continue
        line_indent = len(line) - len(line.lstrip())
        if line_indent <= pip_indent:
            # +1 to account for the newline
            pip_section_end = pip_content_start + sum(
                len(l) + 1 for l in lines_after_pip[:ix]
            )
            break
    else:
        pip_section_end = len(yml_text)
    prefix = yml_text[:pip_content_start]
    pip_portion = yml_text[pip_content_start:pip_section_end]
    suffix = yml_text[pip_section_end:]
    for pkg_to_replace, replacement in REPLACE_REQ_PACKAGES:
        if replacement == None:
            pip_portion = re.sub(
                rf"^(\s*-\s*){re.escape(pkg_to_replace)}([<>~]=?.*|$)\n?",
                "",
                pip_portion,
                flags=re.MULTILINE,
            )
        else:
            pip_portion = re.sub(
                rf"^(\s*-\s*){re.escape(pkg_to_replace)}([<>=!~]=?.*|$)",
                rf"\1{replacement}",
                pip_portion,
                flags=re.MULTILINE,
            )
    return prefix + pip_portion + suffix


def get_environment_yml(instance: dict) -> str:
    """
    Get environment.yml for given task instance

    Args:
        instance (dict): SWE Bench Task instance
    Returns:
        environment.yml (str): Returns environment.yml as string
    """
    # Attempt to find environment.yml at each path based on task instance's repo
    commit = (
        instance["environment_setup_commit"]
        if "environment_setup_commit" in instance
        else instance["base_commit"]
    )
    yml_text = get_environment_yml_by_commit(instance["repo"], commit)
    yml_text = clean_environment_yml(yml_text)
    return yml_text


@cache
def get_requirements_by_commit(repo: str, commit: str) -> str:
    for req_path in MAP_REPO_TO_REQS_PATHS[repo]:
        reqs_url = posixpath.join(SWE_BENCH_URL_RAW, repo, commit, req_path)
        reqs = requests.get(reqs_url, headers=HEADERS)
        if reqs.status_code == 200:
            break
    else:
        raise ValueError(
            f"Could not find requirements.txt at paths {MAP_REPO_TO_REQS_PATHS[repo]} for repo {repo} at commit {commit}"
        )

    lines = reqs.text
    original_req = []
    additional_reqs = []
    req_dir = "/".join(req_path.split("/")[:-1])
    exclude_line = lambda line: any(
        [line.strip().startswith(x) for x in ["-e .", "#", ".[test"]]
    )

    for line in lines.split("\n"):
        if line.strip().startswith("-r"):
            # Handle recursive requirements
            file_name = line[len("-r") :].strip()
            reqs_url = os.path.join(
                SWE_BENCH_URL_RAW,
                repo,
                commit,
                req_dir,
                file_name,
            )
            reqs = requests.get(reqs_url, headers=HEADERS)
            if reqs.status_code == 200:
                for line_extra in reqs.text.split("\n"):
                    if not exclude_line(line_extra):
                        additional_reqs.append(line_extra)
        else:
            if not exclude_line(line):
                original_req.append(line)

    # Combine all requirements into single text body
    additional_reqs.append("\n".join(original_req))
    all_reqs = "\n".join(additional_reqs)

    return all_reqs


def clean_requirements(requirements_text: str) -> str:
    """
    Clean requirements.txt by replacing / removing packages

    E.g. types-pkg_resources has been yanked from PyPI, so we replace it with types-setuptools
    """
    for pkg_to_replace, replacement in REPLACE_REQ_PACKAGES:
        if replacement == None:
            requirements_text = re.sub(
                rf"^{re.escape(pkg_to_replace)}([<>=!~]=?.*|$)\n?",
                "",
                requirements_text,
                flags=re.MULTILINE,
            )
        else:
            # this replacement removes version specifier of the original package
            requirements_text = re.sub(
                rf"^{re.escape(pkg_to_replace)}([<>=!~]=?.*|$)",
                replacement,
                requirements_text,
                flags=re.MULTILINE,
            )
    return requirements_text


def get_requirements(instance: dict) -> str:
    """
    Get requirements.txt for given task instance

    Args:
        instance (dict): task instance
    Returns:
        requirements.txt (str): Returns requirements.txt as string
    """
    # Attempt to find requirements.txt at each path based on task instance's repo
    commit = (
        instance["environment_setup_commit"]
        if "environment_setup_commit" in instance
        else instance["base_commit"]
    )

    requirements_text = get_requirements_by_commit(instance["repo"], commit)
    requirements_text = clean_requirements(requirements_text)
    return requirements_text


def get_test_directives(instance: dict) -> list:
    """
    Get test directives from the test_patch of a task instance

    Args:
        instance (dict): task instance
    Returns:
        directives (list): List of test directives
    """
    # For seq2seq code repos, testing command is fixed
    if instance["repo"] == "swe-bench/humaneval":
        return ["test.py"]

    # Get test directives from test patch and remove non-test files
    diff_pat = r"diff --git a/.* b/(.*)"
    test_patch = instance["test_patch"]
    directives = re.findall(diff_pat, test_patch)
    directives = [
        d for d in directives if not any(d.endswith(ext) for ext in NON_TEST_EXTS)
    ]

    # For Django tests, remove extension + "tests/" prefix and convert slashes to dots (module referencing)
    if instance["repo"] == "django/django":
        directives_transformed = []
        for d in directives:
            d = d[: -len(".py")] if d.endswith(".py") else d
            d = d[len("tests/") :] if d.startswith("tests/") else d
            d = d.replace("/", ".")
            directives_transformed.append(d)
        directives = directives_transformed

    return directives


def make_repo_script_list(specs, repo, base_commit) -> str:
    """
    Create a heredoc-style RUN command to set up the repository for testing.
    This is the setup script for the instance image.
    """
    branch = REPO_BASE_COMMIT_BRANCH.get(repo, {}).get(base_commit, "")
    branch = f"--branch {branch}" if branch else ""
    setup_commands = [
        # Clone and setup repository",
        f"git clone -o origin {branch} --single-branch https://github.com/{repo} {CONTAINER_WORKDIR}",
        f"chmod -R 777 {CONTAINER_WORKDIR}",  # So nonroot user can run tests
        f"cd {CONTAINER_WORKDIR}",
        f"git reset --hard {base_commit}",
        "git remote remove origin",
        f"TARGET_TIMESTAMP=$(git show -s --format=%ci {base_commit})",
        'git tag -l | while read tag; do TAG_COMMIT=$(git rev-list -n 1 "$tag"); TAG_TIME=$(git show -s --format=%ci "$TAG_COMMIT"); if [[ "$TAG_TIME" > "$TARGET_TIMESTAMP" ]]; then git tag -d "$tag"; fi; done',
        "git reflog expire --expire=now --all",
        "git gc --prune=now --aggressive",
        "AFTER_TIMESTAMP=$(date -d \"$TARGET_TIMESTAMP + 1 second\" '+%Y-%m-%d %H:%M:%S')",
        'COMMIT_COUNT=$(git log --oneline --all --since="$AFTER_TIMESTAMP" | wc -l)',
        '[ "$COMMIT_COUNT" -eq 0 ] || exit 1',
        # Setup conda environment and install
        "source /opt/miniconda3/bin/activate",
        f"conda activate {CONTAINER_ENV_NAME}",
        'echo "Current environment: $CONDA_DEFAULT_ENV"',
    ]
    if repo in MAP_REPO_TO_INSTALL:
        setup_commands.append(MAP_REPO_TO_INSTALL[repo])
    if specs.get("pre_install", None):
        for pre_install in specs["pre_install"]:
            setup_commands.append(pre_install)

    if "install" in specs:
        setup_commands.append(specs["install"])

    # If the setup modifies the repository in any way, it can be
    # difficult to get a clean diff.  This ensures that `git diff`
    # will only reflect the changes from the user while retaining the
    # original state of the repository plus setup commands.
    setup_commands += [
        "",
        "# Configure git",
        "git config --global user.email setup@swebench.com",
        "git config --global user.name SWE-bench",
        "git commit --allow-empty -am SWE-bench",
    ]

    return make_heredoc_run_command(setup_commands)


def make_heredoc_run_command(commands: list[str]) -> str:
    """
    Create a heredoc-style RUN command from a list of shell commands.

    Args:
        commands: List of shell commands to execute
    Returns:
        A single heredoc-style RUN command string
    """
    if not commands:
        return ""

    heredoc_content = "\n".join(["#!/bin/bash", "set -euxo pipefail", *commands])
    delimiter = generate_heredoc_delimiter(heredoc_content)
    return f"RUN <<{delimiter}\n{heredoc_content}\n{delimiter}\n"


def load_cached_environment_yml(instance_id: str) -> str:
    """
    Load environment.yml from cache
    """
    conn = sqlite3.connect(
        resources.files(swebench.resources) / "swebench-og" / "environments.yml.db"
    )
    c = conn.cursor()
    c.execute(
        "SELECT environment_yml FROM environments WHERE instance_id = ?", (instance_id,)
    )
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None


def make_env_script_list_from_conda(instance, specs, cached_environment_yml) -> list:
    delimiter = generate_heredoc_delimiter(cached_environment_yml)
    reqs_commands = [
        "source /opt/miniconda3/bin/activate",
        f"cat <<'{delimiter}' > /root/environment.yml\n{cached_environment_yml}\n{delimiter}",
        "conda env create -f /root/environment.yml",
        f"conda activate {CONTAINER_ENV_NAME}",
    ]
    return reqs_commands


def make_env_script_list(instance, specs) -> str:
    """
    Creates a heredoc-style RUN command to set up the conda environment for testing.
    This is the setup script for the environment image.
    """
    cached_environment_yml = load_cached_environment_yml(instance["instance_id"])
    if cached_environment_yml:
        return make_heredoc_run_command(
            make_env_script_list_from_conda(instance, specs, cached_environment_yml)
        )
    reqs_commands = [
        "source /opt/miniconda3/bin/activate",
    ]
    pkgs = specs.get("packages", "")
    if pkgs == "requirements.txt":
        reqs = get_requirements(instance)
        path_to_reqs = "/root/requirements.txt"
        reqs_commands += [
            f"conda create -n {CONTAINER_ENV_NAME} python={specs['python']} -y",
            f"conda activate {CONTAINER_ENV_NAME}",
            "",
            "# Create requirements file",
            f"cat > {path_to_reqs} << 'REQUIREMENTS_EOF'",
            reqs,
            "REQUIREMENTS_EOF",
            "",
            "# Install requirements",
            f"python -m pip install -r {path_to_reqs}",
            f"rm {path_to_reqs}",
        ]
    elif pkgs == "environment.yml":
        reqs = get_environment_yml(instance, CONTAINER_ENV_NAME)
        path_to_reqs = "environment.yml"
        reqs_commands += [f"cat > {path_to_reqs} << 'ENV_EOF'", reqs, "ENV_EOF"]
        if specs.get("no_use_env", None):
            reqs_commands += [
                f"conda create -c conda-forge -n {CONTAINER_ENV_NAME} python={specs['python']} -y",
                f"conda env update -f {path_to_reqs}",
            ]
        else:
            reqs_commands += [
                f"conda env create --file {path_to_reqs}",
                f"conda activate {CONTAINER_ENV_NAME} && conda install python={specs['python']} -y",
            ]
        reqs_commands += [f"rm {path_to_reqs}"]
    else:
        reqs_commands += [
            f"conda create -n {CONTAINER_ENV_NAME} python={specs['python']} {pkgs} -y"
        ]

    reqs_commands.append(f"conda activate {CONTAINER_ENV_NAME}")
    if specs.get("pip_packages", None):
        reqs_commands += [f"python -m pip install {' '.join(specs['pip_packages'])}"]

    return make_heredoc_run_command(reqs_commands)


def make_eval_script_list(instance, specs, base_commit, test_patch) -> list:
    """
    Applies the test patch and runs the tests.
    """
    test_files = get_modified_files(test_patch)
    delimiter = generate_heredoc_delimiter(test_patch)
    apply_test_patch_command = (
        f"git apply -v - <<'{delimiter}'\n{test_patch}\n{delimiter}"
    )
    test_command = " ".join(
        [
            MAP_REPO_VERSION_TO_SPECS[instance["repo"]][instance["version"]][
                "test_cmd"
            ],
            *get_test_directives(instance),
        ]
    )
    eval_commands = [
        "source /opt/miniconda3/bin/activate",
        f"conda activate {CONTAINER_ENV_NAME}",
        f"cd {CONTAINER_WORKDIR}",
    ]
    if "eval_commands" in specs:
        eval_commands += specs["eval_commands"]
    eval_commands += [
        f"git config --global --add safe.directory {CONTAINER_WORKDIR}",  # for nonroot user
        f"cd {CONTAINER_WORKDIR}",
        # This is just informational, so we have a record
        "git status",
        "git show",
        f"git -c core.fileMode=false diff {base_commit}",
        "source /opt/miniconda3/bin/activate",
        f"conda activate {CONTAINER_ENV_NAME}",
    ]
    if "install" in specs:
        eval_commands.append(specs["install"])
    # Reset test files to the state they should be in before the patch.
    reset_tests_command = f"git checkout {base_commit} {' '.join(test_files)}"
    eval_commands += [
        reset_tests_command,
        apply_test_patch_command,
        f": '{START_TEST_OUTPUT}'",
        test_command,
        f": '{END_TEST_OUTPUT}'",
        reset_tests_command,  # Revert tests after done, leave the repo in the same state as before
    ]
    return eval_commands


def _get_dockerfile(instance) -> str:
    repo = instance["repo"]
    version = instance.get("version")
    base_commit = instance["base_commit"]
    specs = MAP_REPO_VERSION_TO_SPECS[repo][version]
    env_script = make_env_script_list(instance, specs)
    repo_script = make_repo_script_list(specs, repo, base_commit)
    dockerfile = _DOCKERFILE_BASE
    dockerfile += f"\n{env_script}\n" if env_script else ""
    dockerfile += '\nRUN echo "source /opt/miniconda3/etc/profile.d/conda.sh && conda activate testbed" > /root/.bashrc\n'
    dockerfile += f"\n{repo_script}\n" if repo_script else ""
    dockerfile += "\nWORKDIR /testbed/\n"
    return dockerfile
