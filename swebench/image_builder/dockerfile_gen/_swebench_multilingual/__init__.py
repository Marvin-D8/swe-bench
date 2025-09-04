from swebench.image_builder.dockerfile_gen._swebench_multilingual.c import (
    _DOCKERFILE_BASE_C,
    MAP_REPO_VERSION_TO_SPECS_C,
)   from swebench.image_builder.dockerfile_gen._swebench_multilingual.go import (
    _DOCKERFILE_BASE_GO,
    MAP_REPO_VERSION_TO_SPECS_GO,
)
from swebench.image_builder.dockerfile_gen._swebench_multilingual.go import (
    _DOCKERFILE_BASE_GO,
    MAP_REPO_VERSION_TO_SPECS_GO,
)
from swebench.image_builder.dockerfile_gen._swebench_multilingual.go import (
    _DOCKERFILE_BASE_GO,
    MAP_REPO_VERSION_TO_SPECS_GO,
)
from swebench.image_builder.dockerfile_gen._swebench_multilingual.java import (
    _DOCKERFILE_BASE_JAVA,
    MAP_REPO_VERSION_TO_SPECS_JAVA,
)
    MAP_REPO_VERSION_TO_SPECS_JAVA,
)
from swebench.image_builder.dockerfile_gen._swebench_multilingual.javascript import (
    _DOCKERFILE_BASE_JS,
    MAP_REPO_VERSION_TO_SPECS_JS,
)
from swebench.image_builder.dockerfile_gen._swebench_multilingual.php import (
    _DOCKERFILE_BASE_PHP,
    MAP_REPO_VERSION_TO_SPECS_PHP,
)
from swebench.image_builder.dockerfile_gen._swebench_multilingual.ruby import (
    _DOCKERFILE_BASE_RUBY,
    MAP_REPO_VERSION_TO_SPECS_RUBY,
)
from swebench.image_builder.dockerfile_gen._swebench_multilingual.rust import (
    _DOCKERFILE_BASE_RUST,
    MAP_REPO_VERSION_TO_SPECS_RUST,
)

MAP_REPO_VERSION_TO_SPECS = {
    **MAP_REPO_VERSION_TO_SPECS_C,
    **MAP_REPO_VERSION_TO_SPECS_GO,
    **MAP_REPO_VERSION_TO_SPECS_JAVA,
    **MAP_REPO_VERSION_TO_SPECS_JS,
    **MAP_REPO_VERSION_TO_SPECS_PHP,
    **MAP_REPO_VERSION_TO_SPECS_RUBY,
    **MAP_REPO_VERSION_TO_SPECS_RUST,
}


def get_dockerfile_base(instance, docker_specs):
    if instance["repo"] in MAP_REPO_VERSION_TO_SPECS_C:
        return _DOCKERFILE_BASE_C.format(**docker_specs)
    elif instance["repo"] in MAP_REPO_VERSION_TO_SPECS_GO:
        return _DOCKERFILE_BASE_GO.format(**docker_specs)
    elif instance["repo"] in MAP_REPO_VERSION_TO_SPECS_JAVA:
        return _DOCKERFILE_BASE_JAVA.format(**docker_specs)
    elif instance["repo"] in MAP_REPO_VERSION_TO_SPECS_JS:
        return _DOCKERFILE_BASE_JS.format(**docker_specs)
    elif instance["repo"] in MAP_REPO_VERSION_TO_SPECS_PHP:
        return _DOCKERFILE_BASE_PHP.format(**docker_specs)
    elif instance["repo"] in MAP_REPO_VERSION_TO_SPECS_RUBY:
        return _DOCKERFILE_BASE_RUBY.format(**docker_specs)
    elif instance["repo"] in MAP_REPO_VERSION_TO_SPECS_RUST:
        return _DOCKERFILE_BASE_RUST.format(**docker_specs)
    else:
        raise ValueError(f"Invalid repository for multilingual: {instance['repo']}")

def make_repo_script_list(
    specs, repo, repo_directory, base_commit, env_name
) -> list:
    """
    Create a list of bash commands to set up the repository for testing.
    This is the setup script for the instance image.
    """
    setup_commands = [
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
    ]
    if "pre_install" in specs:
        setup_commands.extend(specs["pre_install"])
    if "install" in specs:
        setup_commands.extend(specs["install"])
    if "build" in specs:
        setup_commands.extend(specs["build"])
    return setup_commands


def make_env_script_list(instance, specs, env_name) -> list:
    """
    Creates the list of commands to set up the environment for testing.
    This is the setup script for the environment image.
    """
    reqs_commands = []
    if "apt-pkgs" in specs:
        reqs_commands += [
            "apt-get update",
            f"apt-get install -y {' '.join(specs['apt-pkgs'])}",
        ]
    return reqs_commands


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
    monolithic_dockerfile = get_dockerfile_base(instance, docker_specs)
    monolithic_dockerfile += f"\n{env_script}\n" if env_script else ""
    monolithic_dockerfile += "\nRUN echo \"source /opt/miniconda3/etc/profile.d/conda.sh && conda activate testbed\" > /root/.bashrc\n"
    monolithic_dockerfile += f"\n{repo_script}\n" if repo_script else ""
    monolithic_dockerfile += "\nWORKDIR /testbed/\n"
    return monolithic_dockerfile
