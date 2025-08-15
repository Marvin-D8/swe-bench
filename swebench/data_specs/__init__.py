from swebench.data_specs.c import MAP_REPO_VERSION_TO_SPECS_C, MAP_REPO_TO_INSTALL_C
from swebench.data_specs.go import MAP_REPO_VERSION_TO_SPECS_GO, MAP_REPO_TO_INSTALL_GO
from swebench.data_specs.java import MAP_REPO_VERSION_TO_SPECS_JAVA, MAP_REPO_TO_INSTALL_JAVA
from swebench.data_specs.javascript import MAP_REPO_VERSION_TO_SPECS_JS, MAP_REPO_TO_INSTALL_JS
from swebench.data_specs.php import MAP_REPO_VERSION_TO_SPECS_PHP, MAP_REPO_TO_INSTALL_PHP
from swebench.data_specs.python import (
    MAP_REPO_VERSION_TO_SPECS_PY,
    MAP_REPO_TO_INSTALL_PY,
    USE_X86_PY,
    MAP_REPO_TO_REQS_PATHS,
    MAP_REPO_TO_ENV_YML_PATHS,
)
from swebench.data_specs.ruby import MAP_REPO_VERSION_TO_SPECS_RUBY, MAP_REPO_TO_INSTALL_RUBY
from swebench.data_specs.rust import MAP_REPO_VERSION_TO_SPECS_RUST, MAP_REPO_TO_INSTALL_RUST


MAP_REPO_VERSION_TO_SPECS = {
    **MAP_REPO_VERSION_TO_SPECS_C,
    **MAP_REPO_VERSION_TO_SPECS_GO,
    **MAP_REPO_VERSION_TO_SPECS_JAVA,
    **MAP_REPO_VERSION_TO_SPECS_JS,
    **MAP_REPO_VERSION_TO_SPECS_PHP,
    **MAP_REPO_VERSION_TO_SPECS_PY,
    **MAP_REPO_VERSION_TO_SPECS_RUBY,
    **MAP_REPO_VERSION_TO_SPECS_RUST,
}

MAP_REPO_TO_INSTALL = {
    **MAP_REPO_TO_INSTALL_C,
    **MAP_REPO_TO_INSTALL_GO,
    **MAP_REPO_TO_INSTALL_JAVA,
    **MAP_REPO_TO_INSTALL_JS,
    **MAP_REPO_TO_INSTALL_PHP,
    **MAP_REPO_TO_INSTALL_PY,
    **MAP_REPO_TO_INSTALL_RUBY,
    **MAP_REPO_TO_INSTALL_RUST,
}

MAP_REPO_TO_EXT = {
    **{k: "c" for k in MAP_REPO_VERSION_TO_SPECS_C.keys()},
    **{k: "go" for k in MAP_REPO_VERSION_TO_SPECS_GO.keys()},
    **{k: "java" for k in MAP_REPO_VERSION_TO_SPECS_JAVA.keys()},
    **{k: "js" for k in MAP_REPO_VERSION_TO_SPECS_JS.keys()},
    **{k: "php" for k in MAP_REPO_VERSION_TO_SPECS_PHP.keys()},
    **{k: "py" for k in MAP_REPO_VERSION_TO_SPECS_PY.keys()},
    **{k: "rb" for k in MAP_REPO_VERSION_TO_SPECS_RUBY.keys()},
    **{k: "rs" for k in MAP_REPO_VERSION_TO_SPECS_RUST.keys()},
}

USE_X86 = {
    *USE_X86_PY,
}


def get_data_spec(repo, version) -> dict:
    return MAP_REPO_VERSION_TO_SPECS[repo][version]
