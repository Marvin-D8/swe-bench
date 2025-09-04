from functools import cache
from swebench.image_builder.dockerfile_gen._swebench.constants import (
    MAP_REPO_TO_ENV_YML_PATHS,
    MAP_REPO_TO_INSTALL,
    MAP_REPO_TO_REQS_PATHS,
    MAP_REPO_VERSION_TO_SPECS,
    SWE_BENCH_URL_RAW,
    _DOCKERFILE_BASE,
    HEADERS,
    REPLACE_REQ_PACKAGES,
)
from swebench.harness.constants import (
    NON_TEST_EXTS,
    START_TEST_OUTPUT,
    END_TEST_OUTPUT,
)
from swebench.harness.utils import get_modified_files
import posixpath
import requests
import re
import os
from hashlib import blake2b


@cache
def get_environment_yml_by_commit(repo: str, commit: str, env_name: str) -> str:
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
            cleaned.append(f"name: {env_name}")
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


def get_environment_yml(instance: dict, env_name: str) -> str:
    """
    Get environment.yml for given task instance

    Args:
        instance (dict): SWE Bench Task instance
        env_name (str): Rename retrieved environment.yml to this name
    Returns:
        environment.yml (str): Returns environment.yml as string
    """
    # Attempt to find environment.yml at each path based on task instance's repo
    commit = (
        instance["environment_setup_commit"]
        if "environment_setup_commit" in instance
        else instance["base_commit"]
    )
    yml_text = get_environment_yml_by_commit(instance["repo"], commit, env_name)
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


def make_repo_script_list(
    specs, repo, repo_directory, base_commit, env_name
) -> str:
    """
    Create a heredoc-style RUN command to set up the repository for testing.
    This is the setup script for the instance image.
    """
    setup_commands = [
        "# Clone and setup repository",
        f"git clone -o origin --single-branch https://github.com/{repo} {repo_directory}",
        f"chmod -R 777 {repo_directory}",  # So nonroot user can run tests
        f"cd {repo_directory}",
        f"git reset --hard {base_commit}",
        "git remote remove origin",
        "git tag -d $(git tag -l)",
        "git reflog expire --expire=now --all",
        "git gc --prune=now --aggressive",
        f"TARGET_TIMESTAMP=$(git show -s --format=%ci {base_commit})",
        "COMMIT_COUNT=$(git log --oneline --since=\"$TARGET_TIMESTAMP\" | wc -l)",
        "[ \"$COMMIT_COUNT\" -eq 1 ] || exit 1",
        "",
        "# Setup conda environment and install",
        "source /opt/miniconda3/bin/activate",
        f"conda activate {env_name}",
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
    
    heredoc_content = "\n".join([
        "#!/bin/bash",
        "set -euxo pipefail",
        *commands
    ])
    delimiter = f"EOF_{blake2b(heredoc_content.encode()).hexdigest()[:12]}"
    while delimiter in heredoc_content:
        delimiter = f"EOF_{blake2b(heredoc_content.encode() + delimiter.encode()).hexdigest()[:12]}"
    return f"RUN <<{delimiter}\n{heredoc_content}\n{delimiter}\n"


def make_env_script_list(instance, specs, env_name) -> str:
    """
    Creates a heredoc-style RUN command to set up the conda environment for testing.
    This is the setup script for the environment image.
    """
    reqs_commands = [
        "source /opt/miniconda3/bin/activate",
    ]
    pkgs = specs.get("packages", "")
    if pkgs == "requirements.txt":
        reqs = get_requirements(instance)
        path_to_reqs = "/root/requirements.txt"
        reqs_commands += [
            f"conda create -n {env_name} python={specs['python']} -y",
            f"conda activate {env_name}",
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
        reqs = get_environment_yml(instance, env_name)
        path_to_reqs = "environment.yml"
        reqs_commands += [
            f"cat > {path_to_reqs} << 'ENV_EOF'",
            reqs,
            "ENV_EOF"
        ]
        if specs.get("no_use_env", None):
            reqs_commands += [
                f"conda create -c conda-forge -n {env_name} python={specs['python']} -y",
                f"conda env update -f {path_to_reqs}",
            ]
        else:
            reqs_commands += [
                f"conda env create --file {path_to_reqs}",
                f"conda activate {env_name} && conda install python={specs['python']} -y",
            ]
        reqs_commands += [f"rm {path_to_reqs}"]
    else:
        reqs_commands += [f"conda create -n {env_name} python={specs['python']} {pkgs} -y"]
    
    reqs_commands.append(f"conda activate {env_name}")
    if specs.get("pip_packages", None):
        reqs_commands += [f"python -m pip install {' '.join(specs['pip_packages'])}"]
    
    return make_heredoc_run_command(reqs_commands)


def make_eval_script_list(
    instance, specs, env_name, repo_directory, base_commit, test_patch
) -> list:
    """
    Applies the test patch and runs the tests.
    """
    HEREDOC_DELIMITER = "EOF_114329324912"
    test_files = get_modified_files(test_patch)
    # Reset test files to the state they should be in before the patch.
    reset_tests_command = f"git checkout {base_commit} {' '.join(test_files)}"
    apply_test_patch_command = (
        f"git apply -v - <<'{HEREDOC_DELIMITER}'\n{test_patch}\n{HEREDOC_DELIMITER}"
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
        f"conda activate {env_name}",
        f"cd {repo_directory}",
    ]
    if "eval_commands" in specs:
        eval_commands += specs["eval_commands"]
    eval_commands += [
        f"git config --global --add safe.directory {repo_directory}",  # for nonroot user
        f"cd {repo_directory}",
        # This is just informational, so we have a record
        "git status",
        "git show",
        f"git -c core.fileMode=false diff {base_commit}",
        "source /opt/miniconda3/bin/activate",
        f"conda activate {env_name}",
    ]
    if "install" in specs:
        eval_commands.append(specs["install"])
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
    instance_id = instance["instance_id"]
    repo = instance["repo"]
    version = instance.get("version")
    base_commit = instance["base_commit"]
    env_name = "testbed"
    repo_directory = f"/{env_name}"
    specs = MAP_REPO_VERSION_TO_SPECS[repo][version]
    docker_specs = specs.get("docker_specs", {})
    env_script = make_env_script_list(instance, specs, env_name)
    repo_script = make_repo_script_list(
        specs, repo, repo_directory, base_commit, env_name
    )
    monolithic_dockerfile = _DOCKERFILE_BASE
    monolithic_dockerfile += f"\n{env_script}\n" if env_script else ""
    monolithic_dockerfile += "\nRUN echo \"source /opt/miniconda3/etc/profile.d/conda.sh && conda activate testbed\" > /root/.bashrc\n"
    monolithic_dockerfile += f"\n{repo_script}\n" if repo_script else ""
    monolithic_dockerfile += "\nWORKDIR /testbed/\n"
    return monolithic_dockerfile
