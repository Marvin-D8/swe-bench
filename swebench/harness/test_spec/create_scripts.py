from swebench.harness.test_spec.javascript import (
    make_repo_script_list_js,
    make_env_script_list_js,
    make_eval_script_list_js,
)
from swebench.harness.test_spec.python import (
    make_repo_script_list_py,
    make_env_script_list_py,
    make_eval_script_list_py,
)
from swebench.harness.constants import MAP_REPO_TO_EXT


def make_repo_script_list(specs, repo, repo_directory, base_commit, env_name, skip_git_clone=False) -> list:
    """
    Create a list of bash commands to set up the repository for testing.
    This is the setup script for the instance image.
    
    Args:
        specs: Repository specifications
        repo: Repository name
        repo_directory: Directory to clone repository to
        base_commit: Base commit to reset to
        env_name: Conda environment name
        copy_repo_from_host_path: If not None, copy the repository from the host path to the instance image
    """
    ext = MAP_REPO_TO_EXT[repo]
    func = {
        "js": make_repo_script_list_js,
        "py": make_repo_script_list_py,
    }[ext]
    return func(specs, repo, repo_directory, base_commit, env_name, skip_git_clone)


def make_env_script_list(instance, specs, env_name) -> list:
    """
    Creates the list of commands to set up the environment for testing.
    This is the setup script for the environment image.
    """
    ext = MAP_REPO_TO_EXT[instance["repo"]]
    func = {
        "js": make_env_script_list_js,
        "py": make_env_script_list_py,
    }[ext]
    return func(instance, specs, env_name)


def make_eval_script_list(
    instance, specs, env_name, repo_directory, base_commit, test_patch
) -> list:
    """
    Applies the test patch and runs the tests.
    """
    ext = MAP_REPO_TO_EXT[instance["repo"]]
    func = {
        "js": make_eval_script_list_js,
        "py": make_eval_script_list_py,
    }[ext]
    return func(instance, specs, env_name, repo_directory, base_commit, test_patch)
