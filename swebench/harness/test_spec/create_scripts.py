from swebench.data_specs import MAP_REPO_TO_EXT
from swebench.harness.test_spec.javascript import (
    make_eval_script_list_js,
)
from swebench.harness.test_spec.python import (
    make_eval_script_list_py,
)
from swebench.harness.test_spec.utils import (
    make_eval_script_list_common,
)


def make_eval_script_list(
    instance, specs, env_name, repo_directory, base_commit, test_patch
) -> list:
    """
    Applies the test patch and runs the tests.
    """
    ext = MAP_REPO_TO_EXT[instance["repo"]]
    common_func = make_eval_script_list_common
    func = {
        "js": make_eval_script_list_js,
        "py": make_eval_script_list_py,
    }.get(ext, common_func)
    return func(instance, specs, env_name, repo_directory, base_commit, test_patch)
