# Constants - Testing Commands
TEST_PYTEST = "pytest --no-header -rA --tb=no -p no:cacheprovider"
TEST_PYTEST_VERBOSE = "pytest -rA --tb=long -p no:cacheprovider"
TEST_ASTROPY_PYTEST = "pytest -rA -vv -o console_output_style=classic --tb=no"
TEST_DJANGO = "./tests/runtests.py --verbosity 2 --settings=test_sqlite --parallel 1"
TEST_DJANGO_NO_PARALLEL = "./tests/runtests.py --verbosity 2"
TEST_SEABORN = "pytest --no-header -rA"
TEST_SEABORN_VERBOSE = "pytest -rA --tb=long"
TEST_PYTEST = "pytest -rA"
TEST_PYTEST_VERBOSE = "pytest -rA --tb=long"
TEST_SPHINX = "tox --current-env -epy39 -v --"
TEST_SYMPY = (
    "PYTHONWARNINGS='ignore::UserWarning,ignore::SyntaxWarning' bin/test -C --verbose"
)
TEST_SYMPY_VERBOSE = "bin/test -C --verbose"


# Constants - Installation Specifications
SPECS_SKLEARN = {
    k: {
        "python": "3.6",
        "packages": "numpy scipy cython pytest pandas matplotlib",
        "install": "python -m pip install -v --no-use-pep517 --no-build-isolation -e .",
        "pip_packages": [
            "cython",
            "numpy==1.19.2",
            "setuptools",
            "scipy==1.5.2",
        ],
        "test_cmd": TEST_PYTEST,
    }
    for k in ["0.20", "0.21", "0.22"]
}
SPECS_SKLEARN.update(
    {
        k: {
            "python": "3.9",
            "packages": "'numpy==1.19.2' 'scipy==1.5.2' 'cython==3.0.10' pytest 'pandas<2.0.0' 'matplotlib<3.9.0' setuptools pytest joblib threadpoolctl",
            "install": "python -m pip install -v --no-use-pep517 --no-build-isolation -e .",
            "pip_packages": ["cython", "setuptools", "numpy", "scipy"],
            "test_cmd": TEST_PYTEST,
        }
        for k in ["1.3", "1.4", "1.5", "1.6"]
    }
)

SPECS_FLASK = {
    "2.0": {
        "python": "3.9",
        "packages": "requirements.txt",
        "install": "python -m pip install -e .",
        "pip_packages": [
            "setuptools==70.0.0",
            "Werkzeug==2.3.7",
            "Jinja2==3.0.1",
            "itsdangerous==2.1.2",
            "click==8.0.1",
            "MarkupSafe==2.1.3",
        ],
        "test_cmd": TEST_PYTEST,
    },
    "2.1": {
        "python": "3.10",
        "packages": "requirements.txt",
        "install": "python -m pip install -e .",
        "pip_packages": [
            "setuptools==70.0.0",
            "click==8.1.3",
            "itsdangerous==2.1.2",
            "Jinja2==3.1.2",
            "MarkupSafe==2.1.1",
            "Werkzeug==2.3.7",
        ],
        "test_cmd": TEST_PYTEST,
    },
}
SPECS_FLASK.update(
    {
        k: {
            "python": "3.11",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
            "pip_packages": [
                "setuptools==70.0.0",
                "click==8.1.3",
                "itsdangerous==2.1.2",
                "Jinja2==3.1.2",
                "MarkupSafe==2.1.1",
                "Werkzeug==2.3.7",
            ],
            "test_cmd": TEST_PYTEST,
        }
        for k in ["2.2", "2.3", "3.0", "3.1"]
    }
)

SPECS_DJANGO = {
    k: {
        "python": "3.5",
        "packages": "requirements.txt",
        "pre_install": [
            "apt-get update && apt-get install -y locales",
            "echo 'en_US UTF-8' > /etc/locale.gen",
            "locale-gen en_US.UTF-8",
        ],
        "install": "python setup.py install",
        "pip_packages": ["setuptools"],
        "eval_commands": [
            "export LANG=en_US.UTF-8",
            "export LC_ALL=en_US.UTF-8",
            "export PYTHONIOENCODING=utf8",
            "export LANGUAGE=en_US:en",
        ],
        "test_cmd": TEST_DJANGO,
    }
    for k in ["1.7", "1.8", "1.9", "1.10", "1.11", "2.0", "2.1", "2.2"]
}
SPECS_DJANGO.update(
    {
        k: {
            "python": "3.5",
            "install": "python setup.py install",
            "test_cmd": TEST_DJANGO,
        }
        for k in ["1.4", "1.5", "1.6"]
    }
)
SPECS_DJANGO.update(
    {
        k: {
            "python": "3.6",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
            "eval_commands": [
                "sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen",
                "export LANG=en_US.UTF-8",
                "export LANGUAGE=en_US:en",
                "export LC_ALL=en_US.UTF-8",
            ],
            "test_cmd": TEST_DJANGO,
        }
        for k in ["3.0", "3.1", "3.2"]
    }
)
SPECS_DJANGO.update(
    {
        k: {
            "python": "3.8",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
            "test_cmd": TEST_DJANGO,
        }
        for k in ["4.0"]
    }
)
SPECS_DJANGO.update(
    {
        k: {
            "python": "3.9",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
            "test_cmd": TEST_DJANGO,
        }
        for k in ["4.1", "4.2"]
    }
)
SPECS_DJANGO.update(
    {
        k: {
            "python": "3.11",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
            "test_cmd": TEST_DJANGO,
        }
        for k in ["5.0", "5.1", "5.2"]
    }
)
SPECS_DJANGO["1.9"]["test_cmd"] = TEST_DJANGO_NO_PARALLEL

SPECS_REQUESTS = {
    k: {
        "python": "3.9",
        "packages": "pytest",
        "install": "python -m pip install .",
        "test_cmd": TEST_PYTEST,
    }
    for k in ["0.7", "0.8", "0.9", "0.11", "0.13", "0.14", "1.1", "1.2", "2.0", "2.2"]
    + ["2.3", "2.4", "2.5", "2.7", "2.8", "2.9", "2.10", "2.11", "2.12", "2.17"]
    + ["2.18", "2.19", "2.22", "2.26", "2.25", "2.27", "2.31", "3.0"]
}

SPECS_SEABORN = {
    k: {
        "python": "3.9",
        "install": "python -m pip install -e .",
        "pip_packages": [
            "contourpy==1.1.0",
            "cycler==0.11.0",
            "fonttools==4.42.1",
            "importlib-resources==6.0.1",
            "kiwisolver==1.4.5",
            "matplotlib==3.7.2",
            "numpy==1.25.2",
            "packaging==23.1",
            "pandas==1.3.5",  # 2.0.3
            "pillow==10.0.0",
            "pyparsing==3.0.9",
            "pytest",
            "python-dateutil==2.8.2",
            "pytz==2023.3.post1",
            "scipy==1.11.2",
            "six==1.16.0",
            "tzdata==2023.1",
            "zipp==3.16.2",
        ],
        "test_cmd": TEST_SEABORN,
    }
    for k in ["0.11"]
}
SPECS_SEABORN.update(
    {
        k: {
            "python": "3.9",
            "install": "python -m pip install -e .[dev]",
            "pip_packages": [
                "contourpy==1.1.0",
                "cycler==0.11.0",
                "fonttools==4.42.1",
                "importlib-resources==6.0.1",
                "kiwisolver==1.4.5",
                "matplotlib==3.7.2",
                "numpy==1.25.2",
                "packaging==23.1",
                "pandas==2.0.0",
                "pillow==10.0.0",
                "pyparsing==3.0.9",
                "pytest",
                "python-dateutil==2.8.2",
                "pytz==2023.3.post1",
                "scipy==1.11.2",
                "six==1.16.0",
                "tzdata==2023.1",
                "zipp==3.16.2",
            ],
            "test_cmd": TEST_SEABORN,
        }
        for k in ["0.12", "0.13", "0.14"]
    }
)

SPECS_PYTEST = {
    k: {
        "python": "3.9",
        "install": "python -m pip install -e .",
        "test_cmd": TEST_PYTEST,
    }
    for k in [
        "4.4",
        "4.5",
        "4.6",
        "5.0",
        "5.1",
        "5.2",
        "5.3",
        "5.4",
        "6.0",
        "6.2",
        "6.3",
        "7.0",
        "7.1",
        "7.2",
        "7.4",
        "8.0",
        "8.1",
        "8.2",
        "8.3",
        "8.4",
    ]
}
SPECS_PYTEST["4.4"]["pip_packages"] = [
    "atomicwrites==1.4.1",
    "attrs==23.1.0",
    "more-itertools==10.1.0",
    "pluggy==0.13.1",
    "py==1.11.0",
    "setuptools==68.0.0",
    "six==1.16.0",
]
SPECS_PYTEST["4.5"]["pip_packages"] = [
    "atomicwrites==1.4.1",
    "attrs==23.1.0",
    "more-itertools==10.1.0",
    "pluggy==0.11.0",
    "py==1.11.0",
    "setuptools==68.0.0",
    "six==1.16.0",
    "wcwidth==0.2.6",
]
SPECS_PYTEST["4.6"]["pip_packages"] = [
    "atomicwrites==1.4.1",
    "attrs==23.1.0",
    "more-itertools==10.1.0",
    "packaging==23.1",
    "pluggy==0.13.1",
    "py==1.11.0",
    "six==1.16.0",
    "wcwidth==0.2.6",
]
for k in ["5.0", "5.1", "5.2"]:
    SPECS_PYTEST[k]["pip_packages"] = [
        "atomicwrites==1.4.1",
        "attrs==23.1.0",
        "more-itertools==10.1.0",
        "packaging==23.1",
        "pluggy==0.13.1",
        "py==1.11.0",
        "wcwidth==0.2.6",
    ]
SPECS_PYTEST["5.3"]["pip_packages"] = [
    "attrs==23.1.0",
    "more-itertools==10.1.0",
    "packaging==23.1",
    "pluggy==0.13.1",
    "py==1.11.0",
    "wcwidth==0.2.6",
]
SPECS_PYTEST["5.4"]["pip_packages"] = [
    "py==1.11.0",
    "packaging==23.1",
    "attrs==23.1.0",
    "more-itertools==10.1.0",
    "pluggy==0.13.1",
]
SPECS_PYTEST["6.0"]["pip_packages"] = [
    "attrs==23.1.0",
    "iniconfig==2.0.0",
    "more-itertools==10.1.0",
    "packaging==23.1",
    "pluggy==0.13.1",
    "py==1.11.0",
    "toml==0.10.2",
]
for k in ["6.2", "6.3"]:
    SPECS_PYTEST[k]["pip_packages"] = [
        "attrs==23.1.0",
        "iniconfig==2.0.0",
        "packaging==23.1",
        "pluggy==0.13.1",
        "py==1.11.0",
        "toml==0.10.2",
    ]
SPECS_PYTEST["7.0"]["pip_packages"] = [
    "attrs==23.1.0",
    "iniconfig==2.0.0",
    "packaging==23.1",
    "pluggy==0.13.1",
    "py==1.11.0",
]
for k in ["7.1", "7.2"]:
    SPECS_PYTEST[k]["pip_packages"] = [
        "attrs==23.1.0",
        "iniconfig==2.0.0",
        "packaging==23.1",
        "pluggy==0.13.1",
        "py==1.11.0",
        "tomli==2.0.1",
    ]
for k in ["7.4", "8.0", "8.1", "8.2", "8.3", "8.4"]:
    SPECS_PYTEST[k]["pip_packages"] = [
        "iniconfig==2.0.0",
        "packaging==23.1",
        "pluggy==1.3.0",
        "exceptiongroup==1.1.3",
        "tomli==2.0.1",
    ]
SPECS_PYTEST["6.3"]["pre_install"] = ["sed -i 's/>=>=/>=/' setup.cfg"]

SPECS_MATPLOTLIB = {
    k: {
        "python": "3.11",
        "packages": "environment.yml",
        "install": "python -m pip install -e .",
        "pre_install": [
            "apt-get -y update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive apt-get install -y imagemagick ffmpeg texlive texlive-latex-extra texlive-fonts-recommended texlive-xetex texlive-luatex cm-super dvipng",
            'QHULL_URL="http://www.qhull.org/download/qhull-2020-src-8.0.2.tgz"',
            'QHULL_TAR="/tmp/qhull-2020-src-8.0.2.tgz"',
            'QHULL_BUILD_DIR="/testbed/build"',
            'wget -O "$QHULL_TAR" "$QHULL_URL"',
            'mkdir -p "$QHULL_BUILD_DIR"',
            'tar -xvzf "$QHULL_TAR" -C "$QHULL_BUILD_DIR"',
        ],
        "pip_packages": [
            "contourpy==1.1.0",
            "cycler==0.11.0",
            "fonttools==4.42.1",
            "ghostscript",
            "kiwisolver==1.4.5",
            "numpy==1.25.2",
            "packaging==23.1",
            "pillow==10.0.0",
            "pikepdf",
            "pyparsing==3.0.9",
            "python-dateutil==2.8.2",
            "six==1.16.0",
            "setuptools==68.1.2",
            "setuptools-scm==7.1.0",
            "typing-extensions==4.7.1",
        ],
        "test_cmd": TEST_PYTEST,
    }
    for k in ["3.5", "3.6", "3.7", "3.8", "3.9"]
}
SPECS_MATPLOTLIB.update(
    {
        k: {
            "python": "3.8",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
            "pre_install": [
                "apt-get -y update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive apt-get install -y imagemagick ffmpeg libfreetype6-dev pkg-config texlive texlive-latex-extra texlive-fonts-recommended texlive-xetex texlive-luatex cm-super",
                'QHULL_URL="http://www.qhull.org/download/qhull-2020-src-8.0.2.tgz"',
                'QHULL_TAR="/tmp/qhull-2020-src-8.0.2.tgz"',
                'QHULL_BUILD_DIR="/testbed/build"',
                'wget -O "$QHULL_TAR" "$QHULL_URL"',
                'mkdir -p "$QHULL_BUILD_DIR"',
                'tar -xvzf "$QHULL_TAR" -C "$QHULL_BUILD_DIR"',
            ],
            "pip_packages": ["pytest", "ipython"],
            "test_cmd": TEST_PYTEST,
        }
        for k in ["3.1", "3.2", "3.3", "3.4"]
    }
)
SPECS_MATPLOTLIB.update(
    {
        k: {
            "python": "3.7",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
            "pre_install": [
                "apt-get -y update && apt-get -y upgrade && apt-get install -y imagemagick ffmpeg libfreetype6-dev pkg-config",
                'QHULL_URL="http://www.qhull.org/download/qhull-2020-src-8.0.2.tgz"',
                'QHULL_TAR="/tmp/qhull-2020-src-8.0.2.tgz"',
                'QHULL_BUILD_DIR="/testbed/build"',
                'wget -O "$QHULL_TAR" "$QHULL_URL"',
                'mkdir -p "$QHULL_BUILD_DIR"',
                'tar -xvzf "$QHULL_TAR" -C "$QHULL_BUILD_DIR"',
            ],
            "pip_packages": ["pytest"],
            "test_cmd": TEST_PYTEST,
        }
        for k in ["3.0"]
    }
)
SPECS_MATPLOTLIB.update(
    {
        k: {
            "python": "3.5",
            "install": "python setup.py build; python setup.py install",
            "pre_install": [
                "apt-get -y update && apt-get -y upgrade && && apt-get install -y imagemagick ffmpeg"
            ],
            "pip_packages": ["pytest"],
            "execute_test_as_nonroot": True,
            "test_cmd": TEST_PYTEST,
        }
        for k in ["2.0", "2.1", "2.2", "1.0", "1.1", "1.2", "1.3", "1.4", "1.5"]
    }
)
for k in ["3.8", "3.9"]:
    SPECS_MATPLOTLIB[k]["install"] = (
        'python -m pip install --no-build-isolation -e ".[dev]"'
    )

SPECS_SPHINX = {
    k: {
        "python": "3.9",
        "pip_packages": ["tox==4.16.0", "tox-current-env==0.0.11", "Jinja2==3.0.3"],
        "install": "python -m pip install -e .[test]",
        "pre_install": ["sed -i 's/pytest/pytest -rA/' tox.ini"],
        "test_cmd": TEST_SPHINX,
    }
    for k in ["1.5", "1.6", "1.7", "1.8", "2.0", "2.1", "2.2", "2.3", "2.4", "3.0"]
    + ["3.1", "3.2", "3.3", "3.4", "3.5", "4.0", "4.1", "4.2", "4.3", "4.4"]
    + ["4.5", "5.0", "5.1", "5.2", "5.3", "6.0", "6.2", "7.0", "7.1", "7.2"]
    + ["7.3", "7.4", "8.0", "8.1"]
}
for k in ["3.0", "3.1", "3.2", "3.3", "3.4", "3.5", "4.0", "4.1", "4.2", "4.3", "4.4"]:
    SPECS_SPHINX[k]["pre_install"].extend(
        [
            "sed -i 's/Jinja2>=2.3/Jinja2<3.0/' setup.py",
            "sed -i 's/sphinxcontrib-applehelp/sphinxcontrib-applehelp<=1.0.7/' setup.py",
            "sed -i 's/sphinxcontrib-devhelp/sphinxcontrib-devhelp<=1.0.5/' setup.py",
            "sed -i 's/sphinxcontrib-qthelp/sphinxcontrib-qthelp<=1.0.6/' setup.py",
            "sed -i 's/alabaster>=0.7,<0.8/alabaster>=0.7,<0.7.12/' setup.py",
            "sed -i \"s/'packaging',/'packaging', 'markupsafe<=2.0.1',/\" setup.py",
        ]
    )
    if k in ["4.2", "4.3", "4.4"]:
        SPECS_SPHINX[k]["pre_install"].extend(
            [
                "sed -i 's/sphinxcontrib-htmlhelp>=2.0.0/sphinxcontrib-htmlhelp>=2.0.0,<=2.0.4/' setup.py",
                "sed -i 's/sphinxcontrib-serializinghtml>=1.1.5/sphinxcontrib-serializinghtml>=1.1.5,<=1.1.9/' setup.py",
            ]
        )
    elif k == "4.1":
        SPECS_SPHINX[k]["pre_install"].extend(
            [
                (
                    "grep -q 'sphinxcontrib-htmlhelp>=2.0.0' setup.py && "
                    "sed -i 's/sphinxcontrib-htmlhelp>=2.0.0/sphinxcontrib-htmlhelp>=2.0.0,<=2.0.4/' setup.py || "
                    "sed -i 's/sphinxcontrib-htmlhelp/sphinxcontrib-htmlhelp<=2.0.4/' setup.py"
                ),
                (
                    "grep -q 'sphinxcontrib-serializinghtml>=1.1.5' setup.py && "
                    "sed -i 's/sphinxcontrib-serializinghtml>=1.1.5/sphinxcontrib-serializinghtml>=1.1.5,<=1.1.9/' setup.py || "
                    "sed -i 's/sphinxcontrib-serializinghtml/sphinxcontrib-serializinghtml<=1.1.9/' setup.py"
                ),
            ]
        )
    else:
        SPECS_SPHINX[k]["pre_install"].extend(
            [
                "sed -i 's/sphinxcontrib-htmlhelp/sphinxcontrib-htmlhelp<=2.0.4/' setup.py",
                "sed -i 's/sphinxcontrib-serializinghtml/sphinxcontrib-serializinghtml<=1.1.9/' setup.py",
            ]
        )
for k in ["7.2", "7.3", "7.4", "8.0", "8.1"]:
    SPECS_SPHINX[k]["pre_install"] += ["apt-get update && apt-get install -y graphviz"]
for k in ["8.0", "8.1"]:
    SPECS_SPHINX[k]["python"] = "3.10"

SPECS_ASTROPY = {
    k: {
        "python": "3.9",
        "install": "python -m pip install -e .[test] --verbose",
        "pip_packages": [
            "attrs==23.1.0",
            "exceptiongroup==1.1.3",
            "execnet==2.0.2",
            "hypothesis==6.82.6",
            "iniconfig==2.0.0",
            "numpy==1.25.2",
            "packaging==23.1",
            "pluggy==1.3.0",
            "psutil==5.9.5",
            "pyerfa==2.0.0.3",
            "pytest-arraydiff==0.5.0",
            "pytest-astropy-header==0.2.2",
            "pytest-astropy==0.10.0",
            "pytest-cov==4.1.0",
            "pytest-doctestplus==1.0.0",
            "pytest-filter-subpackage==0.1.2",
            "pytest-mock==3.11.1",
            "pytest-openfiles==0.5.0",
            "pytest-remotedata==0.4.0",
            "pytest-xdist==3.3.1",
            "pytest==7.4.0",
            "PyYAML==6.0.1",
            "setuptools==68.0.0",
            "sortedcontainers==2.4.0",
            "tomli==2.0.1",
        ],
        "test_cmd": TEST_PYTEST,
    }
    for k in ["3.0", "3.1", "3.2", "4.1", "4.2", "4.3", "5.0", "5.1", "5.2", "v5.3"]
}
SPECS_ASTROPY.update(
    {
        k: {
            "python": "3.6",
            "install": "python -m pip install -e .[test] --verbose",
            "packages": "setuptools==38.2.4",
            "pip_packages": [
                "attrs==17.3.0",
                "exceptiongroup==0.0.0a0",
                "execnet==1.5.0",
                "hypothesis==3.44.2",
                "cython==0.27.3",
                "jinja2==2.10",
                "MarkupSafe==1.0",
                "numpy==1.16.0",
                "packaging==16.8",
                "pluggy==0.6.0",
                "psutil==5.4.2",
                "pyerfa==1.7.0",
                "pytest-arraydiff==0.1",
                "pytest-astropy-header==0.1",
                "pytest-astropy==0.2.1",
                "pytest-cov==2.5.1",
                "pytest-doctestplus==0.1.2",
                "pytest-filter-subpackage==0.1",
                "pytest-forked==0.2",
                "pytest-mock==1.6.3",
                "pytest-openfiles==0.2.0",
                "pytest-remotedata==0.2.0",
                "pytest-xdist==1.20.1",
                "pytest==3.3.1",
                "PyYAML==3.12",
                "sortedcontainers==1.5.9",
                "tomli==0.2.0",
            ],
            "test_cmd": TEST_ASTROPY_PYTEST,
        }
        for k in ["0.1", "0.2", "0.3", "0.4", "1.1", "1.2", "1.3"]
    }
)
for k in ["4.1", "4.2", "4.3", "5.0", "5.1", "5.2", "v5.3"]:
    SPECS_ASTROPY[k]["pre_install"] = [
        'sed -i \'s/requires = \\["setuptools",/requires = \\["setuptools==68.0.0",/\' pyproject.toml'
    ]
for k in ["v5.3"]:
    SPECS_ASTROPY[k]["python"] = "3.10"

SPECS_SYMPY = {
    k: {
        "python": "3.9",
        "packages": "mpmath flake8",
        "pip_packages": ["mpmath==1.3.0", "flake8-comprehensions"],
        "install": "python -m pip install -e .",
        "test_cmd": TEST_SYMPY,
    }
    for k in ["0.7", "1.0", "1.1", "1.10", "1.11", "1.12", "1.2", "1.4", "1.5", "1.6"]
    + ["1.7", "1.8", "1.9"]
    + ["1.10", "1.11", "1.12", "1.13", "1.14"]
}
SPECS_SYMPY.update(
    {
        k: {
            "python": "3.9",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
            "pip_packages": ["mpmath==1.3.0"],
            "test_cmd": TEST_SYMPY,
        }
        for k in ["1.13", "1.14"]
    }
)

SPECS_PYLINT = {
    k: {
        "python": "3.9",
        "packages": "requirements.txt",
        "install": "python -m pip install -e .",
        "test_cmd": TEST_PYTEST,
    }
    for k in [
        "2.10",
        "2.11",
        "2.13",
        "2.14",
        "2.15",
        "2.16",
        "2.17",
        "2.8",
        "2.9",
        "3.0",
        "3.1",
        "3.2",
        "3.3",
        "4.0",
    ]
}
SPECS_PYLINT["2.8"]["pip_packages"] = ["pyenchant==3.2"]
SPECS_PYLINT["2.8"]["pre_install"] = [
    "apt-get update && apt-get install -y libenchant-2-dev hunspell-en-us"
]
SPECS_PYLINT.update(
    {
        k: {
            **SPECS_PYLINT[k],
            "pip_packages": ["astroid==3.0.0a6", "setuptools"],
        }
        for k in ["3.0", "3.1", "3.2", "3.3", "4.0"]
    }
)
for v in ["2.14", "2.15", "2.17", "3.0", "3.1", "3.2", "3.3", "4.0"]:
    SPECS_PYLINT[v]["nano_cpus"] = int(2e9)

SPECS_XARRAY = {
    k: {
        "python": "3.10",
        "packages": "environment.yml",
        "install": "python -m pip install -e .",
        "pip_packages": [
            "numpy==1.23.0",
            "packaging==23.1",
            "pandas==1.5.3",
            "pytest==7.4.0",
            "python-dateutil==2.8.2",
            "pytz==2023.3",
            "six==1.16.0",
            "scipy==1.11.1",
            "setuptools==68.0.0",
            "dask==2022.8.1",
        ],
        "no_use_env": True,
        "test_cmd": TEST_PYTEST,
    }
    for k in [
        "0.12",
        "0.18",
        "0.19",
        "0.20",
        "2022.03",
        "2022.06",
        "2022.09",
        "2023.07",
        "2024.05",
    ]
}

SPECS_SQLFLUFF = {
    k: {
        "python": "3.9",
        "packages": "requirements.txt",
        "install": "python -m pip install -e .",
        "test_cmd": TEST_PYTEST,
    }
    for k in [
        "0.10",
        "0.11",
        "0.12",
        "0.13",
        "0.4",
        "0.5",
        "0.6",
        "0.8",
        "0.9",
        "1.0",
        "1.1",
        "1.2",
        "1.3",
        "1.4",
        "2.0",
        "2.1",
        "2.2",
    ]
}

SPECS_DBT_CORE = {
    k: {
        "python": "3.9",
        "packages": "requirements.txt",
        "install": "python -m pip install -e .",
    }
    for k in [
        "0.13",
        "0.14",
        "0.15",
        "0.16",
        "0.17",
        "0.18",
        "0.19",
        "0.20",
        "0.21",
        "1.0",
        "1.1",
        "1.2",
        "1.3",
        "1.4",
        "1.5",
        "1.6",
        "1.7",
    ]
}

SPECS_PYVISTA = {
    k: {
        "python": "3.9",
        "install": "python -m pip install -e .",
        "pip_packages": ["pytest"],
        "test_cmd": TEST_PYTEST,
    }
    for k in ["0.20", "0.21", "0.22", "0.23"]
}
SPECS_PYVISTA.update(
    {
        k: {
            "python": "3.9",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
            "pip_packages": ["pytest"],
            "test_cmd": TEST_PYTEST,
            "pre_install": [
                "apt-get update && apt-get install -y ffmpeg libsm6 libxext6 libxrender1"
            ],
        }
        for k in [
            "0.24",
            "0.25",
            "0.26",
            "0.27",
            "0.28",
            "0.29",
            "0.30",
            "0.31",
            "0.32",
            "0.33",
            "0.34",
            "0.35",
            "0.36",
            "0.37",
            "0.38",
            "0.39",
            "0.40",
            "0.41",
            "0.42",
            "0.43",
        ]
    }
)

SPECS_ASTROID = {
    k: {
        "python": "3.9",
        "install": "python -m pip install -e .",
        "pip_packages": ["pytest"],
        "test_cmd": TEST_PYTEST,
    }
    for k in [
        "2.10",
        "2.12",
        "2.13",
        "2.14",
        "2.15",
        "2.16",
        "2.5",
        "2.6",
        "2.7",
        "2.8",
        "2.9",
        "3.0",
    ]
}

SPECS_MARSHMALLOW = {
    k: {
        "python": "3.9",
        "install": "python -m pip install -e '.[dev]'",
        "test_cmd": TEST_PYTEST,
    }
    for k in [
        "2.18",
        "2.19",
        "2.20",
        "3.0",
        "3.1",
        "3.10",
        "3.11",
        "3.12",
        "3.13",
        "3.15",
        "3.16",
        "3.19",
        "3.2",
        "3.4",
        "3.8",
        "3.9",
    ]
}

SPECS_PVLIB = {
    k: {
        "python": "3.9",
        "install": "python -m pip install -e .[all]",
        "packages": "pandas scipy",
        "pip_packages": ["jupyter", "ipython", "matplotlib", "pytest", "flake8"],
        "test_cmd": TEST_PYTEST,
    }
    for k in ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9"]
}

SPECS_PYDICOM = {
    k: {
        "python": "3.6",
        "install": "python -m pip install -e .",
        "packages": "numpy",
        "pip_packages": ["pytest"],
        "test_cmd": TEST_PYTEST,
    }
    for k in [
        "1.0",
        "1.1",
        "1.2",
        "1.3",
        "1.4",
        "2.0",
        "2.1",
        "2.2",
        "2.3",
        "2.4",
        "3.0",
    ]
}
SPECS_PYDICOM.update({k: {**SPECS_PYDICOM[k], "python": "3.8"} for k in ["1.4", "2.0"]})
SPECS_PYDICOM.update({k: {**SPECS_PYDICOM[k], "python": "3.9"} for k in ["2.1", "2.2"]})
SPECS_PYDICOM.update({k: {**SPECS_PYDICOM[k], "python": "3.10"} for k in ["2.3"]})
SPECS_PYDICOM.update(
    {k: {**SPECS_PYDICOM[k], "python": "3.11"} for k in ["2.4", "3.0"]}
)

SPECS_HUMANEVAL = {k: {"python": "3.9", "test_cmd": "python"} for k in ["1.0"]}

# Constants - Task Instance Instllation Environment
MAP_REPO_VERSION_TO_SPECS_PY = {
    "astropy/astropy": SPECS_ASTROPY,
    "dbt-labs/dbt-core": SPECS_DBT_CORE,
    "django/django": SPECS_DJANGO,
    "matplotlib/matplotlib": SPECS_MATPLOTLIB,
    "marshmallow-code/marshmallow": SPECS_MARSHMALLOW,
    "mwaskom/seaborn": SPECS_SEABORN,
    "pallets/flask": SPECS_FLASK,
    "psf/requests": SPECS_REQUESTS,
    "pvlib/pvlib-python": SPECS_PVLIB,
    "pydata/xarray": SPECS_XARRAY,
    "pydicom/pydicom": SPECS_PYDICOM,
    "pylint-dev/astroid": SPECS_ASTROID,
    "pylint-dev/pylint": SPECS_PYLINT,
    "pytest-dev/pytest": SPECS_PYTEST,
    "pyvista/pyvista": SPECS_PYVISTA,
    "scikit-learn/scikit-learn": SPECS_SKLEARN,
    "sphinx-doc/sphinx": SPECS_SPHINX,
    "sqlfluff/sqlfluff": SPECS_SQLFLUFF,
    "swe-bench/humaneval": SPECS_HUMANEVAL,
    "sympy/sympy": SPECS_SYMPY,
}

# Constants - Repository Specific Installation Instructions
MAP_REPO_TO_INSTALL_PY = {}


# Constants - Task Instance Requirements File Paths
MAP_REPO_TO_REQS_PATHS = {
    "dbt-labs/dbt-core": ["dev-requirements.txt", "dev_requirements.txt"],
    "django/django": ["tests/requirements/py3.txt"],
    "matplotlib/matplotlib": [
        "requirements/dev/dev-requirements.txt",
        "requirements/testing/travis_all.txt",
    ],
    "pallets/flask": ["requirements/dev.txt"],
    "pylint-dev/pylint": ["requirements_test.txt"],
    "pyvista/pyvista": ["requirements_test.txt", "requirements.txt"],
    "sqlfluff/sqlfluff": ["requirements_dev.txt"],
    "sympy/sympy": ["requirements-dev.txt", "requirements-test.txt"],
}


# Constants - Task Instance environment.yml File Paths
MAP_REPO_TO_ENV_YML_PATHS = {
    "matplotlib/matplotlib": ["environment.yml"],
    "pydata/xarray": ["ci/requirements/environment.yml", "environment.yml"],
}

USE_X86_PY = {
    "astropy__astropy-7973",
    "django__django-10087",
    "django__django-10097",
    "django__django-10213",
    "django__django-10301",
    "django__django-10316",
    "django__django-10426",
    "django__django-11383",
    "django__django-12185",
    "django__django-12497",
    "django__django-13121",
    "django__django-13417",
    "django__django-13431",
    "django__django-13447",
    "django__django-14155",
    "django__django-14164",
    "django__django-14169",
    "django__django-14170",
    "django__django-15180",
    "django__django-15199",
    "django__django-15280",
    "django__django-15292",
    "django__django-15474",
    "django__django-15682",
    "django__django-15689",
    "django__django-15695",
    "django__django-15698",
    "django__django-15781",
    "django__django-15925",
    "django__django-15930",
    "django__django-5158",
    "django__django-5470",
    "django__django-7188",
    "django__django-7475",
    "django__django-7530",
    "django__django-8326",
    "django__django-8961",
    "django__django-9003",
    "django__django-9703",
    "django__django-9871",
    "matplotlib__matplotlib-13983",
    "matplotlib__matplotlib-13984",
    "matplotlib__matplotlib-13989",
    "matplotlib__matplotlib-14043",
    "matplotlib__matplotlib-14471",
    "matplotlib__matplotlib-22711",
    "matplotlib__matplotlib-22719",
    "matplotlib__matplotlib-22734",
    "matplotlib__matplotlib-22767",
    "matplotlib__matplotlib-22815",
    "matplotlib__matplotlib-22835",
    "matplotlib__matplotlib-22865",
    "matplotlib__matplotlib-22871",
    "matplotlib__matplotlib-22883",
    "matplotlib__matplotlib-22926",
    "matplotlib__matplotlib-22929",
    "matplotlib__matplotlib-22931",
    "matplotlib__matplotlib-22945",
    "matplotlib__matplotlib-22991",
    "matplotlib__matplotlib-23031",
    "matplotlib__matplotlib-23047",
    "matplotlib__matplotlib-23049",
    "matplotlib__matplotlib-23057",
    "matplotlib__matplotlib-23088",
    "matplotlib__matplotlib-23111",
    "matplotlib__matplotlib-23140",
    "matplotlib__matplotlib-23174",
    "matplotlib__matplotlib-23188",
    "matplotlib__matplotlib-23198",
    "matplotlib__matplotlib-23203",
    "matplotlib__matplotlib-23266",
    "matplotlib__matplotlib-23267",
    "matplotlib__matplotlib-23288",
    "matplotlib__matplotlib-23299",
    "matplotlib__matplotlib-23314",
    "matplotlib__matplotlib-23332",
    "matplotlib__matplotlib-23348",
    "matplotlib__matplotlib-23412",
    "matplotlib__matplotlib-23476",
    "matplotlib__matplotlib-23516",
    "matplotlib__matplotlib-23562",
    "matplotlib__matplotlib-23563",
    "matplotlib__matplotlib-23573",
    "matplotlib__matplotlib-23740",
    "matplotlib__matplotlib-23742",
    "matplotlib__matplotlib-23913",
    "matplotlib__matplotlib-23964",
    "matplotlib__matplotlib-23987",
    "matplotlib__matplotlib-24013",
    "matplotlib__matplotlib-24026",
    "matplotlib__matplotlib-24088",
    "matplotlib__matplotlib-24111",
    "matplotlib__matplotlib-24149",
    "matplotlib__matplotlib-24177",
    "matplotlib__matplotlib-24189",
    "matplotlib__matplotlib-24224",
    "matplotlib__matplotlib-24250",
    "matplotlib__matplotlib-24257",
    "matplotlib__matplotlib-24265",
    "matplotlib__matplotlib-24334",
    "matplotlib__matplotlib-24362",
    "matplotlib__matplotlib-24403",
    "matplotlib__matplotlib-24431",
    "matplotlib__matplotlib-24538",
    "matplotlib__matplotlib-24570",
    "matplotlib__matplotlib-24604",
    "matplotlib__matplotlib-24619",
    "matplotlib__matplotlib-24627",
    "matplotlib__matplotlib-24637",
    "matplotlib__matplotlib-24691",
    "matplotlib__matplotlib-24749",
    "matplotlib__matplotlib-24768",
    "matplotlib__matplotlib-24849",
    "matplotlib__matplotlib-24870",
    "matplotlib__matplotlib-24912",
    "matplotlib__matplotlib-24924",
    "matplotlib__matplotlib-24970",
    "matplotlib__matplotlib-24971",
    "matplotlib__matplotlib-25027",
    "matplotlib__matplotlib-25052",
    "matplotlib__matplotlib-25079",
    "matplotlib__matplotlib-25085",
    "matplotlib__matplotlib-25122",
    "matplotlib__matplotlib-25126",
    "matplotlib__matplotlib-25129",
    "matplotlib__matplotlib-25238",
    "matplotlib__matplotlib-25281",
    "matplotlib__matplotlib-25287",
    "matplotlib__matplotlib-25311",
    "matplotlib__matplotlib-25332",
    "matplotlib__matplotlib-25334",
    "matplotlib__matplotlib-25340",
    "matplotlib__matplotlib-25346",
    "matplotlib__matplotlib-25404",
    "matplotlib__matplotlib-25405",
    "matplotlib__matplotlib-25425",
    "matplotlib__matplotlib-25430",
    "matplotlib__matplotlib-25433",
    "matplotlib__matplotlib-25442",
    "matplotlib__matplotlib-25479",
    "matplotlib__matplotlib-25498",
    "matplotlib__matplotlib-25499",
    "matplotlib__matplotlib-25515",
    "matplotlib__matplotlib-25547",
    "matplotlib__matplotlib-25551",
    "matplotlib__matplotlib-25565",
    "matplotlib__matplotlib-25624",
    "matplotlib__matplotlib-25631",
    "matplotlib__matplotlib-25640",
    "matplotlib__matplotlib-25651",
    "matplotlib__matplotlib-25667",
    "matplotlib__matplotlib-25712",
    "matplotlib__matplotlib-25746",
    "matplotlib__matplotlib-25772",
    "matplotlib__matplotlib-25775",
    "matplotlib__matplotlib-25779",
    "matplotlib__matplotlib-25785",
    "matplotlib__matplotlib-25794",
    "matplotlib__matplotlib-25859",
    "matplotlib__matplotlib-25960",
    "matplotlib__matplotlib-26011",
    "matplotlib__matplotlib-26020",
    "matplotlib__matplotlib-26024",
    "matplotlib__matplotlib-26078",
    "matplotlib__matplotlib-26089",
    "matplotlib__matplotlib-26101",
    "matplotlib__matplotlib-26113",
    "matplotlib__matplotlib-26122",
    "matplotlib__matplotlib-26160",
    "matplotlib__matplotlib-26184",
    "matplotlib__matplotlib-26208",
    "matplotlib__matplotlib-26223",
    "matplotlib__matplotlib-26232",
    "matplotlib__matplotlib-26249",
    "matplotlib__matplotlib-26278",
    "matplotlib__matplotlib-26285",
    "matplotlib__matplotlib-26291",
    "matplotlib__matplotlib-26300",
    "matplotlib__matplotlib-26311",
    "matplotlib__matplotlib-26341",
    "matplotlib__matplotlib-26342",
    "matplotlib__matplotlib-26399",
    "matplotlib__matplotlib-26466",
    "matplotlib__matplotlib-26469",
    "matplotlib__matplotlib-26472",
    "matplotlib__matplotlib-26479",
    "matplotlib__matplotlib-26532",
    "pydata__xarray-2905",
    "pydata__xarray-2922",
    "pydata__xarray-3095",
    "pydata__xarray-3114",
    "pydata__xarray-3151",
    "pydata__xarray-3156",
    "pydata__xarray-3159",
    "pydata__xarray-3239",
    "pydata__xarray-3302",
    "pydata__xarray-3305",
    "pydata__xarray-3338",
    "pydata__xarray-3364",
    "pydata__xarray-3406",
    "pydata__xarray-3520",
    "pydata__xarray-3527",
    "pydata__xarray-3631",
    "pydata__xarray-3635",
    "pydata__xarray-3637",
    "pydata__xarray-3649",
    "pydata__xarray-3677",
    "pydata__xarray-3733",
    "pydata__xarray-3812",
    "pydata__xarray-3905",
    "pydata__xarray-3976",
    "pydata__xarray-3979",
    "pydata__xarray-3993",
    "pydata__xarray-4075",
    "pydata__xarray-4094",
    "pydata__xarray-4098",
    "pydata__xarray-4182",
    "pydata__xarray-4184",
    "pydata__xarray-4248",
    "pydata__xarray-4339",
    "pydata__xarray-4356",
    "pydata__xarray-4419",
    "pydata__xarray-4423",
    "pydata__xarray-4442",
    "pydata__xarray-4493",
    "pydata__xarray-4510",
    "pydata__xarray-4629",
    "pydata__xarray-4683",
    "pydata__xarray-4684",
    "pydata__xarray-4687",
    "pydata__xarray-4695",
    "pydata__xarray-4750",
    "pydata__xarray-4758",
    "pydata__xarray-4759",
    "pydata__xarray-4767",
    "pydata__xarray-4802",
    "pydata__xarray-4819",
    "pydata__xarray-4827",
    "pydata__xarray-4879",
    "pydata__xarray-4911",
    "pydata__xarray-4939",
    "pydata__xarray-4940",
    "pydata__xarray-4966",
    "pydata__xarray-4994",
    "pydata__xarray-5033",
    "pydata__xarray-5126",
    "pydata__xarray-5131",
    "pydata__xarray-5180",
    "pydata__xarray-5187",
    "pydata__xarray-5233",
    "pydata__xarray-5362",
    "pydata__xarray-5365",
    "pydata__xarray-5455",
    "pydata__xarray-5580",
    "pydata__xarray-5662",
    "pydata__xarray-5682",
    "pydata__xarray-5731",
    "pydata__xarray-6135",
    "pydata__xarray-6386",
    "pydata__xarray-6394",
    "pydata__xarray-6400",
    "pydata__xarray-6461",
    "pydata__xarray-6548",
    "pydata__xarray-6598",
    "pydata__xarray-6599",
    "pydata__xarray-6601",
    "pydata__xarray-6721",
    "pydata__xarray-6744",
    "pydata__xarray-6798",
    "pydata__xarray-6804",
    "pydata__xarray-6823",
    "pydata__xarray-6857",
    "pydata__xarray-6882",
    "pydata__xarray-6889",
    "pydata__xarray-6938",
    "pydata__xarray-6971",
    "pydata__xarray-6992",
    "pydata__xarray-6999",
    "pydata__xarray-7003",
    "pydata__xarray-7019",
    "pydata__xarray-7052",
    "pydata__xarray-7089",
    "pydata__xarray-7101",
    "pydata__xarray-7105",
    "pydata__xarray-7112",
    "pydata__xarray-7120",
    "pydata__xarray-7147",
    "pydata__xarray-7150",
    "pydata__xarray-7179",
    "pydata__xarray-7203",
    "pydata__xarray-7229",
    "pydata__xarray-7233",
    "pydata__xarray-7347",
    "pydata__xarray-7391",
    "pydata__xarray-7393",
    "pydata__xarray-7400",
    "pydata__xarray-7444",
    "pytest-dev__pytest-10482",
    "scikit-learn__scikit-learn-10198",
    "scikit-learn__scikit-learn-10297",
    "scikit-learn__scikit-learn-10306",
    "scikit-learn__scikit-learn-10331",
    "scikit-learn__scikit-learn-10377",
    "scikit-learn__scikit-learn-10382",
    "scikit-learn__scikit-learn-10397",
    "scikit-learn__scikit-learn-10427",
    "scikit-learn__scikit-learn-10428",
    "scikit-learn__scikit-learn-10443",
    "scikit-learn__scikit-learn-10452",
    "scikit-learn__scikit-learn-10459",
    "scikit-learn__scikit-learn-10471",
    "scikit-learn__scikit-learn-10483",
    "scikit-learn__scikit-learn-10495",
    "scikit-learn__scikit-learn-10508",
    "scikit-learn__scikit-learn-10558",
    "scikit-learn__scikit-learn-10577",
    "scikit-learn__scikit-learn-10581",
    "scikit-learn__scikit-learn-10687",
    "scikit-learn__scikit-learn-10774",
    "scikit-learn__scikit-learn-10777",
    "scikit-learn__scikit-learn-10803",
    "scikit-learn__scikit-learn-10844",
    "scikit-learn__scikit-learn-10870",
    "scikit-learn__scikit-learn-10881",
    "scikit-learn__scikit-learn-10899",
    "scikit-learn__scikit-learn-10908",
    "scikit-learn__scikit-learn-10913",
    "scikit-learn__scikit-learn-10949",
    "scikit-learn__scikit-learn-10982",
    "scikit-learn__scikit-learn-10986",
    "scikit-learn__scikit-learn-11040",
    "scikit-learn__scikit-learn-11042",
    "scikit-learn__scikit-learn-11043",
    "scikit-learn__scikit-learn-11151",
    "scikit-learn__scikit-learn-11160",
    "scikit-learn__scikit-learn-11206",
    "scikit-learn__scikit-learn-11235",
    "scikit-learn__scikit-learn-11243",
    "scikit-learn__scikit-learn-11264",
    "scikit-learn__scikit-learn-11281",
    "scikit-learn__scikit-learn-11310",
    "scikit-learn__scikit-learn-11315",
    "scikit-learn__scikit-learn-11333",
    "scikit-learn__scikit-learn-11346",
    "scikit-learn__scikit-learn-11391",
    "scikit-learn__scikit-learn-11496",
    "scikit-learn__scikit-learn-11542",
    "scikit-learn__scikit-learn-11574",
    "scikit-learn__scikit-learn-11578",
    "scikit-learn__scikit-learn-11585",
    "scikit-learn__scikit-learn-11596",
    "scikit-learn__scikit-learn-11635",
    "scikit-learn__scikit-learn-12258",
    "scikit-learn__scikit-learn-12421",
    "scikit-learn__scikit-learn-12443",
    "scikit-learn__scikit-learn-12462",
    "scikit-learn__scikit-learn-12471",
    "scikit-learn__scikit-learn-12486",
    "scikit-learn__scikit-learn-12557",
    "scikit-learn__scikit-learn-12583",
    "scikit-learn__scikit-learn-12585",
    "scikit-learn__scikit-learn-12625",
    "scikit-learn__scikit-learn-12626",
    "scikit-learn__scikit-learn-12656",
    "scikit-learn__scikit-learn-12682",
    "scikit-learn__scikit-learn-12704",
    "scikit-learn__scikit-learn-12733",
    "scikit-learn__scikit-learn-12758",
    "scikit-learn__scikit-learn-12760",
    "scikit-learn__scikit-learn-12784",
    "scikit-learn__scikit-learn-12827",
    "scikit-learn__scikit-learn-12834",
    "scikit-learn__scikit-learn-12860",
    "scikit-learn__scikit-learn-12908",
    "scikit-learn__scikit-learn-12938",
    "scikit-learn__scikit-learn-12961",
    "scikit-learn__scikit-learn-12973",
    "scikit-learn__scikit-learn-12983",
    "scikit-learn__scikit-learn-12989",
    "scikit-learn__scikit-learn-13010",
    "scikit-learn__scikit-learn-13013",
    "scikit-learn__scikit-learn-13017",
    "scikit-learn__scikit-learn-13046",
    "scikit-learn__scikit-learn-13087",
    "scikit-learn__scikit-learn-13124",
    "scikit-learn__scikit-learn-13135",
    "scikit-learn__scikit-learn-13142",
    "scikit-learn__scikit-learn-13143",
    "scikit-learn__scikit-learn-13157",
    "scikit-learn__scikit-learn-13165",
    "scikit-learn__scikit-learn-13174",
    "scikit-learn__scikit-learn-13221",
    "scikit-learn__scikit-learn-13241",
    "scikit-learn__scikit-learn-13253",
    "scikit-learn__scikit-learn-13280",
    "scikit-learn__scikit-learn-13283",
    "scikit-learn__scikit-learn-13302",
    "scikit-learn__scikit-learn-13313",
    "scikit-learn__scikit-learn-13328",
    "scikit-learn__scikit-learn-13333",
    "scikit-learn__scikit-learn-13363",
    "scikit-learn__scikit-learn-13368",
    "scikit-learn__scikit-learn-13392",
    "scikit-learn__scikit-learn-13436",
    "scikit-learn__scikit-learn-13439",
    "scikit-learn__scikit-learn-13447",
    "scikit-learn__scikit-learn-13454",
    "scikit-learn__scikit-learn-13467",
    "scikit-learn__scikit-learn-13472",
    "scikit-learn__scikit-learn-13485",
    "scikit-learn__scikit-learn-13496",
    "scikit-learn__scikit-learn-13497",
    "scikit-learn__scikit-learn-13536",
    "scikit-learn__scikit-learn-13549",
    "scikit-learn__scikit-learn-13554",
    "scikit-learn__scikit-learn-13584",
    "scikit-learn__scikit-learn-13618",
    "scikit-learn__scikit-learn-13620",
    "scikit-learn__scikit-learn-13628",
    "scikit-learn__scikit-learn-13641",
    "scikit-learn__scikit-learn-13704",
    "scikit-learn__scikit-learn-13726",
    "scikit-learn__scikit-learn-13779",
    "scikit-learn__scikit-learn-13780",
    "scikit-learn__scikit-learn-13828",
    "scikit-learn__scikit-learn-13864",
    "scikit-learn__scikit-learn-13877",
    "scikit-learn__scikit-learn-13910",
    "scikit-learn__scikit-learn-13915",
    "scikit-learn__scikit-learn-13933",
    "scikit-learn__scikit-learn-13960",
    "scikit-learn__scikit-learn-13974",
    "scikit-learn__scikit-learn-13983",
    "scikit-learn__scikit-learn-14012",
    "scikit-learn__scikit-learn-14024",
    "scikit-learn__scikit-learn-14053",
    "scikit-learn__scikit-learn-14067",
    "scikit-learn__scikit-learn-14087",
    "scikit-learn__scikit-learn-14092",
    "scikit-learn__scikit-learn-14114",
    "scikit-learn__scikit-learn-14125",
    "scikit-learn__scikit-learn-14141",
    "scikit-learn__scikit-learn-14237",
    "scikit-learn__scikit-learn-14309",
    "scikit-learn__scikit-learn-14430",
    "scikit-learn__scikit-learn-14450",
    "scikit-learn__scikit-learn-14458",
    "scikit-learn__scikit-learn-14464",
    "scikit-learn__scikit-learn-14496",
    "scikit-learn__scikit-learn-14520",
    "scikit-learn__scikit-learn-14544",
    "scikit-learn__scikit-learn-14591",
    "scikit-learn__scikit-learn-14629",
    "scikit-learn__scikit-learn-14704",
    "scikit-learn__scikit-learn-14706",
    "scikit-learn__scikit-learn-14710",
    "scikit-learn__scikit-learn-14732",
    "scikit-learn__scikit-learn-14764",
    "scikit-learn__scikit-learn-14806",
    "scikit-learn__scikit-learn-14869",
    "scikit-learn__scikit-learn-14878",
    "scikit-learn__scikit-learn-14890",
    "scikit-learn__scikit-learn-14894",
    "scikit-learn__scikit-learn-14898",
    "scikit-learn__scikit-learn-14908",
    "scikit-learn__scikit-learn-14983",
    "scikit-learn__scikit-learn-14999",
    "scikit-learn__scikit-learn-15028",
    "scikit-learn__scikit-learn-15084",
    "scikit-learn__scikit-learn-15086",
    "scikit-learn__scikit-learn-15094",
    "scikit-learn__scikit-learn-15096",
    "scikit-learn__scikit-learn-15100",
    "scikit-learn__scikit-learn-15119",
    "scikit-learn__scikit-learn-15120",
    "scikit-learn__scikit-learn-15138",
    "scikit-learn__scikit-learn-15393",
    "scikit-learn__scikit-learn-15495",
    "scikit-learn__scikit-learn-15512",
    "scikit-learn__scikit-learn-15524",
    "scikit-learn__scikit-learn-15535",
    "scikit-learn__scikit-learn-15625",
    "scikit-learn__scikit-learn-3840",
    "scikit-learn__scikit-learn-7760",
    "scikit-learn__scikit-learn-8554",
    "scikit-learn__scikit-learn-9274",
    "scikit-learn__scikit-learn-9288",
    "scikit-learn__scikit-learn-9304",
    "scikit-learn__scikit-learn-9775",
    "scikit-learn__scikit-learn-9939",
    "sphinx-doc__sphinx-11311",
    "sphinx-doc__sphinx-7910",
    "sympy__sympy-12812",
    "sympy__sympy-14248",
    "sympy__sympy-15222",
    "sympy__sympy-19201",
}

INSTANCE_ID_ENVIRONMENT_YAML = {
    "astropy__astropy-7606": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - certifi=2021.5.30=py36h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.3=he6710b0_2\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=1.1.1w=h7f8727e_0\n  - pip=21.2.2=py36h06a4308_0\n  - python=3.6.13=h12debd9_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=38.2.4=py36_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - wheel=0.37.1=pyhd3eb1b0_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - apipkg==2.1.1\n      - async-generator==1.10\n      - attrs==17.3.0\n      - contextvars==2.4\n      - coverage==6.2\n      - cython==0.27.3\n      - exceptiongroup==0.0.0a0\n      - execnet==1.5.0\n      - hypothesis==3.44.2\n      - idna==3.10\n      - immutables==0.19\n      - jinja2==2.10\n      - markupsafe==1.0\n      - numpy==1.16.0\n      - outcome==1.0.0\n      - packaging==16.8\n      - pluggy==0.6.0\n      - psutil==5.4.2\n      - py==1.11.0\n      - pyerfa==1.7.0\n      - pyparsing==3.1.4\n      - pytest==3.3.1\n      - pytest-arraydiff==0.1\n      - pytest-cov==2.5.1\n      - pytest-doctestplus==0.1.2\n      - pytest-filter-subpackage==0.1\n      - pytest-forked==0.2\n      - pytest-mock==1.6.3\n      - pytest-openfiles==0.2.0\n      - pytest-remotedata==0.2.0\n      - pytest-xdist==1.20.1\n      - pyyaml==3.12\n      - six==1.16.0\n      - sniffio==1.2.0\n      - sortedcontainers==1.5.9\n      - tomli==0.2.0\n      - trio==0.8.0\n      - typing-extensions==4.1.1\nprefix: /opt/miniconda3/envs/testbed",
    "astropy__astropy-8707": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - asttokens==2.4.1\n      - attrs==23.1.0\n      - certifi==2024.8.30\n      - contourpy==1.3.0\n      - coverage==7.6.2\n      - cycler==0.12.1\n      - decorator==5.1.1\n      - exceptiongroup==1.1.3\n      - execnet==2.0.2\n      - executing==2.1.0\n      - fonttools==4.54.1\n      - hypothesis==6.82.6\n      - importlib-resources==6.4.5\n      - iniconfig==2.0.0\n      - ipython==8.18.1\n      - jedi==0.19.1\n      - jinja2==3.1.4\n      - jplephem==2.22\n      - kiwisolver==1.4.7\n      - markupsafe==3.0.2\n      - matplotlib==3.9.2\n      - matplotlib-inline==0.1.7\n      - numpy==1.25.2\n      - objgraph==3.6.2\n      - packaging==23.1\n      - parso==0.8.4\n      - pexpect==4.9.0\n      - pillow==11.0.0\n      - pluggy==1.3.0\n      - prompt-toolkit==3.0.48\n      - psutil==5.9.5\n      - ptyprocess==0.7.0\n      - pure-eval==0.2.3\n      - pyerfa==2.0.0.3\n      - pygments==2.18.0\n      - pyparsing==3.2.0\n      - pytest==7.4.0\n      - pytest-arraydiff==0.5.0\n      - pytest-cov==4.1.0\n      - pytest-doctestplus==1.0.0\n      - pytest-filter-subpackage==0.1.2\n      - pytest-mock==3.11.1\n      - pytest-mpl==0.17.0\n      - pytest-openfiles==0.5.0\n      - pytest-remotedata==0.4.0\n      - pytest-xdist==3.3.1\n      - python-dateutil==2.9.0.post0\n      - pyyaml==6.0.1\n      - setuptools==68.0.0\n      - sgp4==2.23\n      - six==1.16.0\n      - skyfield==1.49\n      - sortedcontainers==2.4.0\n      - stack-data==0.6.3\n      - tomli==2.0.1\n      - traitlets==5.14.3\n      - typing-extensions==4.12.2\n      - wcwidth==0.2.13\n      - zipp==3.20.2\nprefix: /opt/miniconda3/envs/testbed",
    "astropy__astropy-8872": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - asttokens==2.4.1\n      - attrs==23.1.0\n      - certifi==2024.8.30\n      - contourpy==1.3.0\n      - coverage==7.6.2\n      - cycler==0.12.1\n      - decorator==5.1.1\n      - exceptiongroup==1.1.3\n      - execnet==2.0.2\n      - executing==2.1.0\n      - fonttools==4.54.1\n      - hypothesis==6.82.6\n      - importlib-resources==6.4.5\n      - iniconfig==2.0.0\n      - ipython==8.18.1\n      - jedi==0.19.1\n      - jinja2==3.1.4\n      - jplephem==2.22\n      - kiwisolver==1.4.7\n      - markupsafe==3.0.2\n      - matplotlib==3.9.2\n      - matplotlib-inline==0.1.7\n      - numpy==1.25.2\n      - objgraph==3.6.2\n      - packaging==23.1\n      - parso==0.8.4\n      - pexpect==4.9.0\n      - pillow==11.0.0\n      - pluggy==1.3.0\n      - prompt-toolkit==3.0.48\n      - psutil==5.9.5\n      - ptyprocess==0.7.0\n      - pure-eval==0.2.3\n      - pyerfa==2.0.0.3\n      - pygments==2.18.0\n      - pyparsing==3.2.0\n      - pytest==7.4.0\n      - pytest-arraydiff==0.5.0\n      - pytest-cov==4.1.0\n      - pytest-doctestplus==1.0.0\n      - pytest-filter-subpackage==0.1.2\n      - pytest-mock==3.11.1\n      - pytest-mpl==0.17.0\n      - pytest-openfiles==0.5.0\n      - pytest-remotedata==0.4.0\n      - pytest-xdist==3.3.1\n      - python-dateutil==2.9.0.post0\n      - pyyaml==6.0.1\n      - setuptools==68.0.0\n      - sgp4==2.23\n      - six==1.16.0\n      - skyfield==1.49\n      - sortedcontainers==2.4.0\n      - stack-data==0.6.3\n      - tomli==2.0.1\n      - traitlets==5.14.3\n      - typing-extensions==4.12.2\n      - wcwidth==0.2.13\n      - zipp==3.20.2\nprefix: /opt/miniconda3/envs/testbed",
    "django__django-10097": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - certifi=2020.6.20=pyhd3eb1b0_3\n  - libffi=3.3=he6710b0_2\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=1.1.1w=h7f8727e_0\n  - pip=10.0.1=py35_0\n  - python=3.5.6=h12debd9_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=40.2.0=py35_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - wheel=0.37.1=pyhd3eb1b0_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - argon2-cffi==21.1.0\n      - bcrypt==3.1.7\n      - cffi==1.15.1\n      - chardet==4.0.0\n      - docutils==0.18.1\n      - geoip2==3.0.0\n      - idna==2.10\n      - jinja2==2.11.3\n      - markupsafe==1.1.1\n      - maxminddb==2.0.0\n      - numpy==1.18.5\n      - pillow==7.2.0\n      - pycparser==2.21\n      - pylibmc==1.6.1\n      - python-memcached==1.62\n      - pytz==2024.2\n      - pywatchman==1.4.1\n      - pyyaml==5.3.1\n      - requests==2.25.1\n      - selenium==3.141.0\n      - six==1.16.0\n      - sqlparse==0.4.4\n      - tblib==1.7.0\n      - urllib3==1.26.9\nprefix: /opt/miniconda3/envs/testbed",
    "psf__requests-1724": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - exceptiongroup=1.2.0=py39h06a4308_0\n  - iniconfig=1.1.1=pyhd3eb1b0_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - packaging=24.1=py39h06a4308_0\n  - pip=24.2=py39h06a4308_0\n  - pluggy=1.0.0=py39h06a4308_1\n  - pytest=7.4.4=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tomli=2.0.1=py39h06a4308_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\nprefix: /opt/miniconda3/envs/testbed",
    "psf__requests-1766": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - exceptiongroup=1.2.0=py39h06a4308_0\n  - iniconfig=1.1.1=pyhd3eb1b0_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - packaging=24.1=py39h06a4308_0\n  - pip=24.2=py39h06a4308_0\n  - pluggy=1.0.0=py39h06a4308_1\n  - pytest=7.4.4=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tomli=2.0.1=py39h06a4308_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\nprefix: /opt/miniconda3/envs/testbed",
    "psf__requests-2317": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - exceptiongroup=1.2.0=py39h06a4308_0\n  - iniconfig=1.1.1=pyhd3eb1b0_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - packaging=24.1=py39h06a4308_0\n  - pip=24.2=py39h06a4308_0\n  - pluggy=1.0.0=py39h06a4308_1\n  - pytest=7.4.4=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tomli=2.0.1=py39h06a4308_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\nprefix: /opt/miniconda3/envs/testbed",
    "pydata__xarray-2905": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=conda_forge\n  - _openmp_mutex=4.5=2_gnu\n  - affine=2.4.0=pyhd8ed1ab_0\n  - aiobotocore=2.15.1=pyhd8ed1ab_0\n  - aiohappyeyeballs=2.4.3=pyhd8ed1ab_0\n  - aiohttp=3.10.9=py310ha75aee5_0\n  - aioitertools=0.12.0=pyhd8ed1ab_0\n  - aiosignal=1.3.1=pyhd8ed1ab_0\n  - antlr-python-runtime=4.11.1=pyhd8ed1ab_0\n  - appdirs=1.4.4=pyh9f0ad1d_0\n  - asciitree=0.3.3=py_2\n  - async-timeout=4.0.3=pyhd8ed1ab_0\n  - attrs=24.2.0=pyh71513ae_0\n  - aws-c-auth=0.7.31=h57bd9a3_0\n  - aws-c-cal=0.7.4=hfd43aa1_1\n  - aws-c-common=0.9.28=hb9d3cd8_0\n  - aws-c-compression=0.2.19=h756ea98_1\n  - aws-c-event-stream=0.4.3=h29ce20c_2\n  - aws-c-http=0.8.10=h5e77a74_0\n  - aws-c-io=0.14.18=h4e6ae90_11\n  - aws-c-mqtt=0.10.7=h02abb05_0\n  - aws-c-s3=0.6.6=h834ce55_0\n  - aws-c-sdkutils=0.1.19=h756ea98_3\n  - aws-checksums=0.1.20=h756ea98_0\n  - aws-crt-cpp=0.28.3=h3e6eb3e_6\n  - aws-sdk-cpp=1.11.407=h9f1560d_0\n  - azure-core-cpp=1.13.0=h935415a_0\n  - azure-identity-cpp=1.9.0=hd126650_0\n  - azure-storage-blobs-cpp=12.13.0=h1d30c4a_0\n  - azure-storage-common-cpp=12.8.0=ha3822c6_0\n  - azure-storage-files-datalake-cpp=12.12.0=h0f25b8a_0\n  - backports.zoneinfo=0.2.1=py310hff52083_9\n  - beautifulsoup4=4.12.3=pyha770c72_0\n  - blosc=1.21.6=hef167b5_0\n  - bokeh=3.5.2=pyhd8ed1ab_0\n  - boto3=1.35.23=pyhd8ed1ab_0\n  - botocore=1.35.23=pyge310_1234567_0\n  - bottleneck=1.4.0=py310hf462985_2\n  - brotli=1.1.0=hb9d3cd8_2\n  - brotli-bin=1.1.0=hb9d3cd8_2\n  - brotli-python=1.1.0=py310hf71b8c6_2\n  - bzip2=1.0.8=h4bc722e_7\n  - c-ares=1.33.1=heb4867d_0\n  - ca-certificates=2024.8.30=hbcca054_0\n  - cached-property=1.5.2=hd8ed1ab_1\n  - cached_property=1.5.2=pyha770c72_1\n  - cartopy=0.24.0=py310h5eaa309_0\n  - cdat_info=8.2.1=pyhd8ed1ab_2\n  - cdms2=3.1.5=py310h366d46e_22\n  - cdtime=3.1.4=py310h7a088e3_13\n  - certifi=2024.8.30=pyhd8ed1ab_0\n  - cf-units=3.2.0=py310hf462985_6\n  - cffi=1.17.1=py310h8deb56e_0\n  - cfgrib=0.9.14.1=pyhd8ed1ab_0\n  - cfgv=3.3.1=pyhd8ed1ab_0\n  - cftime=1.6.4=py310hf462985_1\n  - charset-normalizer=3.4.0=pyhd8ed1ab_0\n  - click=8.1.7=unix_pyh707e725_0\n  - click-plugins=1.1.1=py_0\n  - cligj=0.7.2=pyhd8ed1ab_1\n  - cloudpickle=3.0.0=pyhd8ed1ab_0\n  - colorama=0.4.6=pyhd8ed1ab_0\n  - contourpy=1.3.0=py310h3788b33_2\n  - coverage=7.6.1=py310ha75aee5_1\n  - curl=8.10.1=hbbe4b11_0\n  - cycler=0.12.1=pyhd8ed1ab_0\n  - cytoolz=1.0.0=py310ha75aee5_1\n  - dask-expr=1.1.15=pyhd8ed1ab_0\n  - distarray=2.12.2=pyh050c7b8_4\n  - distlib=0.3.8=pyhd8ed1ab_0\n  - distributed=2024.9.1=pyhd8ed1ab_0\n  - docopt-ng=0.9.0=pyhd8ed1ab_0\n  - eccodes=2.38.0=h8bb6dbc_0\n  - esmf=8.6.1=nompi_h4441c20_3\n  - esmpy=8.6.1=pyhc1e730c_0\n  - exceptiongroup=1.2.2=pyhd8ed1ab_0\n  - execnet=2.1.1=pyhd8ed1ab_0\n  - fasteners=0.17.3=pyhd8ed1ab_0\n  - filelock=3.16.1=pyhd8ed1ab_0\n  - findlibs=0.0.5=pyhd8ed1ab_0\n  - flexcache=0.3=pyhd8ed1ab_0\n  - flexparser=0.3.1=pyhd8ed1ab_0\n  - fonttools=4.54.1=py310ha75aee5_0\n  - freeglut=3.2.2=ha6d2627_3\n  - freetype=2.12.1=h267a509_2\n  - freexl=2.0.0=h743c826_0\n  - frozenlist=1.4.1=py310ha75aee5_1\n  - fsspec=2024.9.0=pyhff2d567_0\n  - future=1.0.0=pyhd8ed1ab_0\n  - g2clib=1.9.0=ha770c72_1\n  - geos=3.13.0=h5888daf_0\n  - geotiff=1.7.3=h77b800c_3\n  - gflags=2.2.2=h5888daf_1005\n  - giflib=5.2.2=hd590300_0\n  - glog=0.7.1=hbabe93e_0\n  - h2=4.1.0=pyhd8ed1ab_0\n  - h5netcdf=1.4.0=pyhd8ed1ab_0\n  - h5py=3.11.0=nompi_py310hf054cd7_102\n  - hdf4=4.2.15=h2a13503_7\n  - hdf5=1.14.3=nompi_hdf9ad27_105\n  - hpack=4.0.0=pyh9f0ad1d_0\n  - hyperframe=6.0.1=pyhd8ed1ab_0\n  - hypothesis=6.114.0=pyha770c72_0\n  - icu=75.1=he02047a_0\n  - identify=2.6.1=pyhd8ed1ab_0\n  - idna=3.10=pyhd8ed1ab_0\n  - importlib-metadata=8.5.0=pyha770c72_0\n  - importlib-resources=6.4.5=pyhd8ed1ab_0\n  - importlib_metadata=8.5.0=hd8ed1ab_0\n  - importlib_resources=6.4.5=pyhd8ed1ab_0\n  - iniconfig=2.0.0=pyhd8ed1ab_0\n  - iris=3.10.0=pyha770c72_1\n  - jasper=4.2.4=h536e39c_0\n  - jinja2=3.1.4=pyhd8ed1ab_0\n  - jmespath=1.0.1=pyhd8ed1ab_0\n  - json-c=0.18=h6688a6e_0\n  - jsonschema=4.23.0=pyhd8ed1ab_0\n  - jsonschema-specifications=2024.10.1=pyhd8ed1ab_0\n  - jupyter_core=5.7.2=pyh31011fe_1\n  - keyutils=1.6.1=h166bdaf_0\n  - kiwisolver=1.4.7=py310h3788b33_0\n  - krb5=1.21.3=h659f571_0\n  - lazy-object-proxy=1.10.0=py310h2372a71_0\n  - lcms2=2.16=hb7c19ff_0\n  - ld_impl_linux-64=2.43=h712a8e2_1\n  - lerc=4.0.0=h27087fc_0\n  - libabseil=20240722.0=cxx17_h5888daf_1\n  - libaec=1.1.3=h59595ed_0\n  - libarchive=3.7.4=hfca40fe_0\n  - libarrow=17.0.0=h364f349_19_cpu\n  - libarrow-acero=17.0.0=h5888daf_19_cpu\n  - libarrow-dataset=17.0.0=h5888daf_19_cpu\n  - libarrow-substrait=17.0.0=he882d9a_19_cpu\n  - libblas=3.9.0=24_linux64_openblas\n  - libbrotlicommon=1.1.0=hb9d3cd8_2\n  - libbrotlidec=1.1.0=hb9d3cd8_2\n  - libbrotlienc=1.1.0=hb9d3cd8_2\n  - libcblas=3.9.0=24_linux64_openblas\n  - libcdms=3.1.2=h0cec689_129\n  - libcf=1.0.3=py310h1588dd5_117\n  - libcrc32c=1.1.2=h9c3ff4c_0\n  - libcurl=8.10.1=hbbe4b11_0\n  - libdeflate=1.22=hb9d3cd8_0\n  - libedit=3.1.20191231=he28a2e2_2\n  - libev=4.33=hd590300_2\n  - libevent=2.1.12=hf998b51_1\n  - libexpat=2.6.3=h5888daf_0\n  - libffi=3.4.2=h7f98852_5\n  - libgcc=14.1.0=h77fa898_1\n  - libgcc-ng=14.1.0=h69a702a_1\n  - libgdal-core=3.9.2=hd5b9bfb_7\n  - libgfortran=14.1.0=h69a702a_1\n  - libgfortran-ng=14.1.0=h69a702a_1\n  - libgfortran5=14.1.0=hc5f4f2c_1\n  - libglu=9.0.0=ha6d2627_1004\n  - libgomp=14.1.0=h77fa898_1\n  - libgoogle-cloud=2.29.0=h438788a_1\n  - libgoogle-cloud-storage=2.29.0=h0121fbd_1\n  - libgrpc=1.65.5=hf5c653b_0\n  - libiconv=1.17=hd590300_2\n  - libjpeg-turbo=3.0.0=hd590300_1\n  - libkml=1.3.0=hf539b9f_1021\n  - liblapack=3.9.0=24_linux64_openblas\n  - libllvm14=14.0.6=hcd5def8_4\n  - libnetcdf=4.9.2=nompi_h135f659_114\n  - libnghttp2=1.58.0=h47da74e_1\n  - libnsl=2.0.1=hd590300_0\n  - libopenblas=0.3.27=pthreads_hac2b453_1\n  - libparquet=17.0.0=h6bd9018_19_cpu\n  - libpng=1.6.44=hadc24fc_0\n  - libprotobuf=5.27.5=h5b01275_2\n  - libre2-11=2023.11.01=hbbce691_0\n  - librttopo=1.1.0=h97f6797_17\n  - libspatialite=5.1.0=h1b4f908_11\n  - libsqlite=3.46.1=hadc24fc_0\n  - libssh2=1.11.0=h0841786_0\n  - libstdcxx=14.1.0=hc0a3c3a_1\n  - libstdcxx-ng=14.1.0=h4852527_1\n  - libthrift=0.21.0=h0e7cc3e_0\n  - libtiff=4.7.0=he137b08_1\n  - libudunits2=2.2.28=h40f5838_3\n  - libutf8proc=2.8.0=h166bdaf_0\n  - libuuid=2.38.1=h0b41bf4_0\n  - libwebp-base=1.4.0=hd590300_0\n  - libxcb=1.17.0=h8a09558_0\n  - libxcrypt=4.4.36=hd590300_1\n  - libxml2=2.12.7=he7c6b58_4\n  - libxslt=1.1.39=h76b75d6_0\n  - libzip=1.11.1=hf83b1b0_0\n  - libzlib=1.3.1=hb9d3cd8_2\n  - llvmlite=0.43.0=py310h1a6248f_1\n  - locket=1.0.0=pyhd8ed1ab_0\n  - lxml=5.3.0=py310h6ee67d5_1\n  - lz4=4.3.3=py310hb259640_1\n  - lz4-c=1.9.4=hcb278e6_0\n  - lzo=2.10=hd590300_1001\n  - markupsafe=3.0.1=py310h89163eb_1\n  - matplotlib-base=3.9.2=py310h68603db_1\n  - minizip=4.0.7=h401b404_0\n  - msgpack-python=1.1.0=py310h3788b33_0\n  - multidict=6.1.0=py310ha75aee5_0\n  - munkres=1.1.4=pyh9f0ad1d_0\n  - nbformat=5.10.4=pyhd8ed1ab_0\n  - nc-time-axis=1.4.1=pyhd8ed1ab_0\n  - nceplibs-g2c=1.9.0=ha39ef1c_1\n  - ncurses=6.5=he02047a_1\n  - netcdf-fortran=4.6.1=nompi_h22f9119_106\n  - netcdf4=1.7.1=nompi_py310h9f0ad05_102\n  - nodeenv=1.9.1=pyhd8ed1ab_0\n  - nomkl=1.0=h5ca1d4c_0\n  - numba=0.60.0=py310h5dc88bb_0\n  - numcodecs=0.13.0=py310h0cd1892_0\n  - numexpr=2.10.0=py310h3ea09b0_100\n  - openblas=0.3.27=pthreads_h9eca1d5_1\n  - openjpeg=2.5.2=h488ebb8_0\n  - openssl=3.3.2=hb9d3cd8_0\n  - orc=2.0.2=h690cf93_1\n  - partd=1.4.2=pyhd8ed1ab_0\n  - patsy=0.5.6=pyhd8ed1ab_0\n  - pcre2=10.44=hba22ea6_2\n  - pillow=10.4.0=py310he228d35_1\n  - pint=0.24.3=pyhd8ed1ab_0\n  - pip=24.2=pyh8b19718_1\n  - pkgutil-resolve-name=1.3.10=pyhd8ed1ab_1\n  - platformdirs=4.3.6=pyhd8ed1ab_0\n  - pluggy=1.5.0=pyhd8ed1ab_0\n  - pooch=1.8.2=pyhd8ed1ab_0\n  - pre-commit=4.0.1=pyha770c72_0\n  - proj=9.5.0=h12925eb_0\n  - pseudonetcdf=3.4.0=pyhd8ed1ab_0\n  - psutil=6.0.0=py310ha75aee5_1\n  - pthread-stubs=0.4=hb9d3cd8_1002\n  - pyarrow=17.0.0=py310hb7f781d_1\n  - pyarrow-core=17.0.0=py310h85d79f8_1_cpu\n  - pyarrow-hotfix=0.6=pyhd8ed1ab_0\n  - pycparser=2.22=pyhd8ed1ab_0\n  - pydap=3.5=pyhd8ed1ab_0\n  - pyparsing=3.1.4=pyhd8ed1ab_0\n  - pyproj=3.7.0=py310h2e9f774_0\n  - pyshp=2.3.1=pyhd8ed1ab_0\n  - pysocks=1.7.1=pyha2e5f31_6\n  - pytest-cov=5.0.0=pyhd8ed1ab_0\n  - pytest-env=1.1.5=pyhd8ed1ab_0\n  - pytest-xdist=3.6.1=pyhd8ed1ab_0\n  - python=3.10.15=h4a871b0_1_cpython\n  - python-eccodes=2.37.0=py310hf462985_0\n  - python-fastjsonschema=2.20.0=pyhd8ed1ab_0\n  - python-tzdata=2024.2=pyhd8ed1ab_0\n  - python-xxhash=3.5.0=py310ha75aee5_1\n  - python_abi=3.10=5_cp310\n  - pyyaml=6.0.2=py310ha75aee5_1\n  - qhull=2020.2=h434a139_5\n  - rasterio=1.4.1=py310hf6c6cbe_0\n  - re2=2023.11.01=h77b4e00_0\n  - readline=8.2=h8228510_1\n  - referencing=0.35.1=pyhd8ed1ab_0\n  - requests=2.32.3=pyhd8ed1ab_0\n  - rpds-py=0.20.0=py310h505e2c1_1\n  - s2n=1.5.4=h1380c3d_0\n  - s3transfer=0.10.3=pyhd8ed1ab_0\n  - seaborn=0.13.2=hd8ed1ab_2\n  - seaborn-base=0.13.2=pyhd8ed1ab_2\n  - shapely=2.0.6=py310had3dfd6_2\n  - six=1.16.0=pyh6c4a22f_0\n  - snappy=1.2.1=ha2e4443_0\n  - snuggs=1.4.7=pyhd8ed1ab_1\n  - sortedcontainers=2.4.0=pyhd8ed1ab_0\n  - soupsieve=2.5=pyhd8ed1ab_1\n  - sparse=0.15.4=pyh267e887_1\n  - sqlite=3.46.1=h9eae976_0\n  - statsmodels=0.14.4=py310hf462985_0\n  - tblib=3.0.0=pyhd8ed1ab_0\n  - tk=8.6.13=noxft_h4845f30_101\n  - toml=0.10.2=pyhd8ed1ab_0\n  - tomli=2.0.2=pyhd8ed1ab_0\n  - toolz=1.0.0=pyhd8ed1ab_0\n  - tornado=6.4.1=py310ha75aee5_1\n  - traitlets=5.14.3=pyhd8ed1ab_0\n  - typing-extensions=4.12.2=hd8ed1ab_0\n  - typing_extensions=4.12.2=pyha770c72_0\n  - tzdata=2024b=hc8b5060_0\n  - udunits2=2.2.28=h40f5838_3\n  - ukkonen=1.0.1=py310h3788b33_5\n  - unicodedata2=15.1.0=py310h2372a71_0\n  - uriparser=0.9.8=hac33072_0\n  - urllib3=2.2.3=pyhd8ed1ab_0\n  - virtualenv=20.26.6=pyhd8ed1ab_0\n  - webob=1.8.8=pyhd8ed1ab_0\n  - wheel=0.44.0=pyhd8ed1ab_0\n  - wrapt=1.16.0=py310ha75aee5_1\n  - xerces-c=3.2.5=h988505b_2\n  - xorg-libx11=1.8.10=h4f16b4b_0\n  - xorg-libxau=1.0.11=hb9d3cd8_1\n  - xorg-libxdmcp=1.1.5=hb9d3cd8_0\n  - xorg-libxext=1.3.6=hb9d3cd8_0\n  - xorg-libxfixes=6.0.1=hb9d3cd8_0\n  - xorg-libxi=1.8.2=hb9d3cd8_0\n  - xorg-xextproto=7.3.0=hb9d3cd8_1004\n  - xorg-xorgproto=2024.1=hb9d3cd8_1\n  - xxhash=0.8.2=hd590300_0\n  - xyzservices=2024.9.0=pyhd8ed1ab_0\n  - xz=5.2.6=h166bdaf_0\n  - yaml=0.2.5=h7f98852_2\n  - yarl=1.13.1=py310ha75aee5_0\n  - zarr=2.18.3=pyhd8ed1ab_0\n  - zict=3.0.0=pyhd8ed1ab_0\n  - zipp=3.20.2=pyhd8ed1ab_0\n  - zlib=1.3.1=hb9d3cd8_2\n  - zstandard=0.23.0=py310ha39cb0e_1\n  - zstd=1.5.6=ha6fb4c9_0\n  - pip:\n      - dask==2022.8.1\n      - numbagg==0.8.2\n      - numpy==1.23.0\n      - packaging==23.1\n      - pandas==1.5.3\n      - pytest==7.4.0\n      - python-dateutil==2.8.2\n      - pytz==2023.3\n      - scipy==1.11.1\n      - setuptools==68.0.0\nprefix: /opt/miniconda3/envs/testbed",
    "pydata__xarray-3305": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=conda_forge\n  - _openmp_mutex=4.5=2_gnu\n  - affine=2.4.0=pyhd8ed1ab_0\n  - aiobotocore=2.15.1=pyhd8ed1ab_0\n  - aiohappyeyeballs=2.4.3=pyhd8ed1ab_0\n  - aiohttp=3.10.9=py310ha75aee5_0\n  - aioitertools=0.12.0=pyhd8ed1ab_0\n  - aiosignal=1.3.1=pyhd8ed1ab_0\n  - antlr-python-runtime=4.11.1=pyhd8ed1ab_0\n  - appdirs=1.4.4=pyh9f0ad1d_0\n  - asciitree=0.3.3=py_2\n  - async-timeout=4.0.3=pyhd8ed1ab_0\n  - attrs=24.2.0=pyh71513ae_0\n  - aws-c-auth=0.7.31=h57bd9a3_0\n  - aws-c-cal=0.7.4=hfd43aa1_1\n  - aws-c-common=0.9.28=hb9d3cd8_0\n  - aws-c-compression=0.2.19=h756ea98_1\n  - aws-c-event-stream=0.4.3=h29ce20c_2\n  - aws-c-http=0.8.10=h5e77a74_0\n  - aws-c-io=0.14.18=h4e6ae90_11\n  - aws-c-mqtt=0.10.7=h02abb05_0\n  - aws-c-s3=0.6.6=h834ce55_0\n  - aws-c-sdkutils=0.1.19=h756ea98_3\n  - aws-checksums=0.1.20=h756ea98_0\n  - aws-crt-cpp=0.28.3=h3e6eb3e_6\n  - aws-sdk-cpp=1.11.407=h9f1560d_0\n  - azure-core-cpp=1.13.0=h935415a_0\n  - azure-identity-cpp=1.9.0=hd126650_0\n  - azure-storage-blobs-cpp=12.13.0=h1d30c4a_0\n  - azure-storage-common-cpp=12.8.0=ha3822c6_0\n  - azure-storage-files-datalake-cpp=12.12.0=h0f25b8a_0\n  - backports.zoneinfo=0.2.1=py310hff52083_9\n  - beautifulsoup4=4.12.3=pyha770c72_0\n  - blosc=1.21.6=hef167b5_0\n  - bokeh=3.5.2=pyhd8ed1ab_0\n  - boto3=1.35.23=pyhd8ed1ab_0\n  - botocore=1.35.23=pyge310_1234567_0\n  - bottleneck=1.4.0=py310hf462985_2\n  - brotli=1.1.0=hb9d3cd8_2\n  - brotli-bin=1.1.0=hb9d3cd8_2\n  - brotli-python=1.1.0=py310hf71b8c6_2\n  - bzip2=1.0.8=h4bc722e_7\n  - c-ares=1.33.1=heb4867d_0\n  - ca-certificates=2024.8.30=hbcca054_0\n  - cached-property=1.5.2=hd8ed1ab_1\n  - cached_property=1.5.2=pyha770c72_1\n  - cartopy=0.24.0=py310h5eaa309_0\n  - cdat_info=8.2.1=pyhd8ed1ab_2\n  - cdms2=3.1.5=py310h366d46e_22\n  - cdtime=3.1.4=py310h7a088e3_13\n  - certifi=2024.8.30=pyhd8ed1ab_0\n  - cf-units=3.2.0=py310hf462985_6\n  - cffi=1.17.1=py310h8deb56e_0\n  - cfgrib=0.9.14.1=pyhd8ed1ab_0\n  - cfgv=3.3.1=pyhd8ed1ab_0\n  - cftime=1.6.4=py310hf462985_1\n  - charset-normalizer=3.4.0=pyhd8ed1ab_0\n  - click=8.1.7=unix_pyh707e725_0\n  - click-plugins=1.1.1=py_0\n  - cligj=0.7.2=pyhd8ed1ab_1\n  - cloudpickle=3.0.0=pyhd8ed1ab_0\n  - colorama=0.4.6=pyhd8ed1ab_0\n  - contourpy=1.3.0=py310h3788b33_2\n  - coverage=7.6.1=py310ha75aee5_1\n  - curl=8.10.1=hbbe4b11_0\n  - cycler=0.12.1=pyhd8ed1ab_0\n  - cytoolz=1.0.0=py310ha75aee5_1\n  - dask-expr=1.1.15=pyhd8ed1ab_0\n  - distarray=2.12.2=pyh050c7b8_4\n  - distlib=0.3.8=pyhd8ed1ab_0\n  - distributed=2024.9.1=pyhd8ed1ab_0\n  - docopt-ng=0.9.0=pyhd8ed1ab_0\n  - eccodes=2.38.0=h8bb6dbc_0\n  - esmf=8.6.1=nompi_h4441c20_3\n  - esmpy=8.6.1=pyhc1e730c_0\n  - exceptiongroup=1.2.2=pyhd8ed1ab_0\n  - execnet=2.1.1=pyhd8ed1ab_0\n  - fasteners=0.17.3=pyhd8ed1ab_0\n  - filelock=3.16.1=pyhd8ed1ab_0\n  - findlibs=0.0.5=pyhd8ed1ab_0\n  - flexcache=0.3=pyhd8ed1ab_0\n  - flexparser=0.3.1=pyhd8ed1ab_0\n  - fonttools=4.54.1=py310ha75aee5_0\n  - freeglut=3.2.2=ha6d2627_3\n  - freetype=2.12.1=h267a509_2\n  - freexl=2.0.0=h743c826_0\n  - frozenlist=1.4.1=py310ha75aee5_1\n  - fsspec=2024.9.0=pyhff2d567_0\n  - future=1.0.0=pyhd8ed1ab_0\n  - g2clib=1.9.0=ha770c72_1\n  - geos=3.13.0=h5888daf_0\n  - geotiff=1.7.3=h77b800c_3\n  - gflags=2.2.2=h5888daf_1005\n  - giflib=5.2.2=hd590300_0\n  - glog=0.7.1=hbabe93e_0\n  - h2=4.1.0=pyhd8ed1ab_0\n  - h5netcdf=1.4.0=pyhd8ed1ab_0\n  - h5py=3.11.0=nompi_py310hf054cd7_102\n  - hdf4=4.2.15=h2a13503_7\n  - hdf5=1.14.3=nompi_hdf9ad27_105\n  - hpack=4.0.0=pyh9f0ad1d_0\n  - hyperframe=6.0.1=pyhd8ed1ab_0\n  - hypothesis=6.114.0=pyha770c72_0\n  - icu=75.1=he02047a_0\n  - identify=2.6.1=pyhd8ed1ab_0\n  - idna=3.10=pyhd8ed1ab_0\n  - importlib-metadata=8.5.0=pyha770c72_0\n  - importlib-resources=6.4.5=pyhd8ed1ab_0\n  - importlib_metadata=8.5.0=hd8ed1ab_0\n  - importlib_resources=6.4.5=pyhd8ed1ab_0\n  - iniconfig=2.0.0=pyhd8ed1ab_0\n  - iris=3.10.0=pyha770c72_1\n  - jasper=4.2.4=h536e39c_0\n  - jinja2=3.1.4=pyhd8ed1ab_0\n  - jmespath=1.0.1=pyhd8ed1ab_0\n  - json-c=0.18=h6688a6e_0\n  - jsonschema=4.23.0=pyhd8ed1ab_0\n  - jsonschema-specifications=2024.10.1=pyhd8ed1ab_0\n  - jupyter_core=5.7.2=pyh31011fe_1\n  - keyutils=1.6.1=h166bdaf_0\n  - kiwisolver=1.4.7=py310h3788b33_0\n  - krb5=1.21.3=h659f571_0\n  - lazy-object-proxy=1.10.0=py310h2372a71_0\n  - lcms2=2.16=hb7c19ff_0\n  - ld_impl_linux-64=2.43=h712a8e2_1\n  - lerc=4.0.0=h27087fc_0\n  - libabseil=20240722.0=cxx17_h5888daf_1\n  - libaec=1.1.3=h59595ed_0\n  - libarchive=3.7.4=hfca40fe_0\n  - libarrow=17.0.0=h364f349_19_cpu\n  - libarrow-acero=17.0.0=h5888daf_19_cpu\n  - libarrow-dataset=17.0.0=h5888daf_19_cpu\n  - libarrow-substrait=17.0.0=he882d9a_19_cpu\n  - libblas=3.9.0=24_linux64_openblas\n  - libbrotlicommon=1.1.0=hb9d3cd8_2\n  - libbrotlidec=1.1.0=hb9d3cd8_2\n  - libbrotlienc=1.1.0=hb9d3cd8_2\n  - libcblas=3.9.0=24_linux64_openblas\n  - libcdms=3.1.2=h0cec689_129\n  - libcf=1.0.3=py310h1588dd5_117\n  - libcrc32c=1.1.2=h9c3ff4c_0\n  - libcurl=8.10.1=hbbe4b11_0\n  - libdeflate=1.22=hb9d3cd8_0\n  - libedit=3.1.20191231=he28a2e2_2\n  - libev=4.33=hd590300_2\n  - libevent=2.1.12=hf998b51_1\n  - libexpat=2.6.3=h5888daf_0\n  - libffi=3.4.2=h7f98852_5\n  - libgcc=14.1.0=h77fa898_1\n  - libgcc-ng=14.1.0=h69a702a_1\n  - libgdal-core=3.9.2=hd5b9bfb_7\n  - libgfortran=14.1.0=h69a702a_1\n  - libgfortran-ng=14.1.0=h69a702a_1\n  - libgfortran5=14.1.0=hc5f4f2c_1\n  - libglu=9.0.0=ha6d2627_1004\n  - libgomp=14.1.0=h77fa898_1\n  - libgoogle-cloud=2.29.0=h438788a_1\n  - libgoogle-cloud-storage=2.29.0=h0121fbd_1\n  - libgrpc=1.65.5=hf5c653b_0\n  - libiconv=1.17=hd590300_2\n  - libjpeg-turbo=3.0.0=hd590300_1\n  - libkml=1.3.0=hf539b9f_1021\n  - liblapack=3.9.0=24_linux64_openblas\n  - libllvm14=14.0.6=hcd5def8_4\n  - libnetcdf=4.9.2=nompi_h135f659_114\n  - libnghttp2=1.58.0=h47da74e_1\n  - libnsl=2.0.1=hd590300_0\n  - libopenblas=0.3.27=pthreads_hac2b453_1\n  - libparquet=17.0.0=h6bd9018_19_cpu\n  - libpng=1.6.44=hadc24fc_0\n  - libprotobuf=5.27.5=h5b01275_2\n  - libre2-11=2023.11.01=hbbce691_0\n  - librttopo=1.1.0=h97f6797_17\n  - libspatialite=5.1.0=h1b4f908_11\n  - libsqlite=3.46.1=hadc24fc_0\n  - libssh2=1.11.0=h0841786_0\n  - libstdcxx=14.1.0=hc0a3c3a_1\n  - libstdcxx-ng=14.1.0=h4852527_1\n  - libthrift=0.21.0=h0e7cc3e_0\n  - libtiff=4.7.0=he137b08_1\n  - libudunits2=2.2.28=h40f5838_3\n  - libutf8proc=2.8.0=h166bdaf_0\n  - libuuid=2.38.1=h0b41bf4_0\n  - libwebp-base=1.4.0=hd590300_0\n  - libxcb=1.17.0=h8a09558_0\n  - libxcrypt=4.4.36=hd590300_1\n  - libxml2=2.12.7=he7c6b58_4\n  - libxslt=1.1.39=h76b75d6_0\n  - libzip=1.11.1=hf83b1b0_0\n  - libzlib=1.3.1=hb9d3cd8_2\n  - llvmlite=0.43.0=py310h1a6248f_1\n  - locket=1.0.0=pyhd8ed1ab_0\n  - lxml=5.3.0=py310h6ee67d5_1\n  - lz4=4.3.3=py310hb259640_1\n  - lz4-c=1.9.4=hcb278e6_0\n  - lzo=2.10=hd590300_1001\n  - markupsafe=3.0.1=py310h89163eb_1\n  - matplotlib-base=3.9.2=py310h68603db_1\n  - minizip=4.0.7=h401b404_0\n  - msgpack-python=1.1.0=py310h3788b33_0\n  - multidict=6.1.0=py310ha75aee5_0\n  - munkres=1.1.4=pyh9f0ad1d_0\n  - nbformat=5.10.4=pyhd8ed1ab_0\n  - nc-time-axis=1.4.1=pyhd8ed1ab_0\n  - nceplibs-g2c=1.9.0=ha39ef1c_1\n  - ncurses=6.5=he02047a_1\n  - netcdf-fortran=4.6.1=nompi_h22f9119_106\n  - netcdf4=1.7.1=nompi_py310h9f0ad05_102\n  - nodeenv=1.9.1=pyhd8ed1ab_0\n  - nomkl=1.0=h5ca1d4c_0\n  - numba=0.60.0=py310h5dc88bb_0\n  - numcodecs=0.13.0=py310h0cd1892_0\n  - numexpr=2.10.0=py310h3ea09b0_100\n  - openblas=0.3.27=pthreads_h9eca1d5_1\n  - openjpeg=2.5.2=h488ebb8_0\n  - openssl=3.3.2=hb9d3cd8_0\n  - orc=2.0.2=h690cf93_1\n  - partd=1.4.2=pyhd8ed1ab_0\n  - patsy=0.5.6=pyhd8ed1ab_0\n  - pcre2=10.44=hba22ea6_2\n  - pillow=10.4.0=py310he228d35_1\n  - pint=0.24.3=pyhd8ed1ab_0\n  - pip=24.2=pyh8b19718_1\n  - pkgutil-resolve-name=1.3.10=pyhd8ed1ab_1\n  - platformdirs=4.3.6=pyhd8ed1ab_0\n  - pluggy=1.5.0=pyhd8ed1ab_0\n  - pooch=1.8.2=pyhd8ed1ab_0\n  - pre-commit=4.0.1=pyha770c72_0\n  - proj=9.5.0=h12925eb_0\n  - pseudonetcdf=3.4.0=pyhd8ed1ab_0\n  - psutil=6.0.0=py310ha75aee5_1\n  - pthread-stubs=0.4=hb9d3cd8_1002\n  - pyarrow=17.0.0=py310hb7f781d_1\n  - pyarrow-core=17.0.0=py310h85d79f8_1_cpu\n  - pyarrow-hotfix=0.6=pyhd8ed1ab_0\n  - pycparser=2.22=pyhd8ed1ab_0\n  - pydap=3.5=pyhd8ed1ab_0\n  - pyparsing=3.1.4=pyhd8ed1ab_0\n  - pyproj=3.7.0=py310h2e9f774_0\n  - pyshp=2.3.1=pyhd8ed1ab_0\n  - pysocks=1.7.1=pyha2e5f31_6\n  - pytest-cov=5.0.0=pyhd8ed1ab_0\n  - pytest-env=1.1.5=pyhd8ed1ab_0\n  - pytest-xdist=3.6.1=pyhd8ed1ab_0\n  - python=3.10.15=h4a871b0_1_cpython\n  - python-eccodes=2.37.0=py310hf462985_0\n  - python-fastjsonschema=2.20.0=pyhd8ed1ab_0\n  - python-tzdata=2024.2=pyhd8ed1ab_0\n  - python-xxhash=3.5.0=py310ha75aee5_1\n  - python_abi=3.10=5_cp310\n  - pyyaml=6.0.2=py310ha75aee5_1\n  - qhull=2020.2=h434a139_5\n  - rasterio=1.4.1=py310hf6c6cbe_0\n  - re2=2023.11.01=h77b4e00_0\n  - readline=8.2=h8228510_1\n  - referencing=0.35.1=pyhd8ed1ab_0\n  - requests=2.32.3=pyhd8ed1ab_0\n  - rpds-py=0.20.0=py310h505e2c1_1\n  - s2n=1.5.4=h1380c3d_0\n  - s3transfer=0.10.3=pyhd8ed1ab_0\n  - seaborn=0.13.2=hd8ed1ab_2\n  - seaborn-base=0.13.2=pyhd8ed1ab_2\n  - shapely=2.0.6=py310had3dfd6_2\n  - six=1.16.0=pyh6c4a22f_0\n  - snappy=1.2.1=ha2e4443_0\n  - snuggs=1.4.7=pyhd8ed1ab_1\n  - sortedcontainers=2.4.0=pyhd8ed1ab_0\n  - soupsieve=2.5=pyhd8ed1ab_1\n  - sparse=0.15.4=pyh267e887_1\n  - sqlite=3.46.1=h9eae976_0\n  - statsmodels=0.14.4=py310hf462985_0\n  - tblib=3.0.0=pyhd8ed1ab_0\n  - tk=8.6.13=noxft_h4845f30_101\n  - toml=0.10.2=pyhd8ed1ab_0\n  - tomli=2.0.2=pyhd8ed1ab_0\n  - toolz=1.0.0=pyhd8ed1ab_0\n  - tornado=6.4.1=py310ha75aee5_1\n  - traitlets=5.14.3=pyhd8ed1ab_0\n  - typing-extensions=4.12.2=hd8ed1ab_0\n  - typing_extensions=4.12.2=pyha770c72_0\n  - tzdata=2024b=hc8b5060_0\n  - udunits2=2.2.28=h40f5838_3\n  - ukkonen=1.0.1=py310h3788b33_5\n  - unicodedata2=15.1.0=py310h2372a71_0\n  - uriparser=0.9.8=hac33072_0\n  - urllib3=2.2.3=pyhd8ed1ab_0\n  - virtualenv=20.26.6=pyhd8ed1ab_0\n  - webob=1.8.8=pyhd8ed1ab_0\n  - wheel=0.44.0=pyhd8ed1ab_0\n  - wrapt=1.16.0=py310ha75aee5_1\n  - xerces-c=3.2.5=h988505b_2\n  - xorg-libx11=1.8.10=h4f16b4b_0\n  - xorg-libxau=1.0.11=hb9d3cd8_1\n  - xorg-libxdmcp=1.1.5=hb9d3cd8_0\n  - xorg-libxext=1.3.6=hb9d3cd8_0\n  - xorg-libxfixes=6.0.1=hb9d3cd8_0\n  - xorg-libxi=1.8.2=hb9d3cd8_0\n  - xorg-xextproto=7.3.0=hb9d3cd8_1004\n  - xorg-xorgproto=2024.1=hb9d3cd8_1\n  - xxhash=0.8.2=hd590300_0\n  - xyzservices=2024.9.0=pyhd8ed1ab_0\n  - xz=5.2.6=h166bdaf_0\n  - yaml=0.2.5=h7f98852_2\n  - yarl=1.13.1=py310ha75aee5_0\n  - zarr=2.18.3=pyhd8ed1ab_0\n  - zict=3.0.0=pyhd8ed1ab_0\n  - zipp=3.20.2=pyhd8ed1ab_0\n  - zlib=1.3.1=hb9d3cd8_2\n  - zstandard=0.23.0=py310ha39cb0e_1\n  - zstd=1.5.6=ha6fb4c9_0\n  - pip:\n      - dask==2022.8.1\n      - numbagg==0.8.2\n      - numpy==1.23.0\n      - packaging==23.1\n      - pandas==1.5.3\n      - pytest==7.4.0\n      - python-dateutil==2.8.2\n      - pytz==2023.3\n      - scipy==1.11.1\n      - setuptools==68.0.0\nprefix: /opt/miniconda3/envs/testbed",
    "pydata__xarray-3993": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=conda_forge\n  - _openmp_mutex=4.5=2_gnu\n  - affine=2.4.0=pyhd8ed1ab_0\n  - aiobotocore=2.15.1=pyhd8ed1ab_0\n  - aiohappyeyeballs=2.4.3=pyhd8ed1ab_0\n  - aiohttp=3.10.9=py310ha75aee5_0\n  - aioitertools=0.12.0=pyhd8ed1ab_0\n  - aiosignal=1.3.1=pyhd8ed1ab_0\n  - antlr-python-runtime=4.11.1=pyhd8ed1ab_0\n  - appdirs=1.4.4=pyh9f0ad1d_0\n  - asciitree=0.3.3=py_2\n  - async-timeout=4.0.3=pyhd8ed1ab_0\n  - attrs=24.2.0=pyh71513ae_0\n  - aws-c-auth=0.7.31=h57bd9a3_0\n  - aws-c-cal=0.7.4=hfd43aa1_1\n  - aws-c-common=0.9.28=hb9d3cd8_0\n  - aws-c-compression=0.2.19=h756ea98_1\n  - aws-c-event-stream=0.4.3=h29ce20c_2\n  - aws-c-http=0.8.10=h5e77a74_0\n  - aws-c-io=0.14.18=h4e6ae90_11\n  - aws-c-mqtt=0.10.7=h02abb05_0\n  - aws-c-s3=0.6.6=h834ce55_0\n  - aws-c-sdkutils=0.1.19=h756ea98_3\n  - aws-checksums=0.1.20=h756ea98_0\n  - aws-crt-cpp=0.28.3=h3e6eb3e_6\n  - aws-sdk-cpp=1.11.407=h9f1560d_0\n  - azure-core-cpp=1.13.0=h935415a_0\n  - azure-identity-cpp=1.9.0=hd126650_0\n  - azure-storage-blobs-cpp=12.13.0=h1d30c4a_0\n  - azure-storage-common-cpp=12.8.0=ha3822c6_0\n  - azure-storage-files-datalake-cpp=12.12.0=h0f25b8a_0\n  - backports.zoneinfo=0.2.1=py310hff52083_9\n  - beautifulsoup4=4.12.3=pyha770c72_0\n  - blosc=1.21.6=hef167b5_0\n  - bokeh=3.5.2=pyhd8ed1ab_0\n  - boto3=1.35.23=pyhd8ed1ab_0\n  - botocore=1.35.23=pyge310_1234567_0\n  - bottleneck=1.4.0=py310hf462985_2\n  - brotli=1.1.0=hb9d3cd8_2\n  - brotli-bin=1.1.0=hb9d3cd8_2\n  - brotli-python=1.1.0=py310hf71b8c6_2\n  - bzip2=1.0.8=h4bc722e_7\n  - c-ares=1.33.1=heb4867d_0\n  - ca-certificates=2024.8.30=hbcca054_0\n  - cached-property=1.5.2=hd8ed1ab_1\n  - cached_property=1.5.2=pyha770c72_1\n  - cartopy=0.24.0=py310h5eaa309_0\n  - cdat_info=8.2.1=pyhd8ed1ab_2\n  - cdms2=3.1.5=py310h366d46e_22\n  - cdtime=3.1.4=py310h7a088e3_13\n  - certifi=2024.8.30=pyhd8ed1ab_0\n  - cf-units=3.2.0=py310hf462985_6\n  - cffi=1.17.1=py310h8deb56e_0\n  - cfgrib=0.9.14.1=pyhd8ed1ab_0\n  - cfgv=3.3.1=pyhd8ed1ab_0\n  - cftime=1.6.4=py310hf462985_1\n  - charset-normalizer=3.4.0=pyhd8ed1ab_0\n  - click=8.1.7=unix_pyh707e725_0\n  - click-plugins=1.1.1=py_0\n  - cligj=0.7.2=pyhd8ed1ab_1\n  - cloudpickle=3.0.0=pyhd8ed1ab_0\n  - colorama=0.4.6=pyhd8ed1ab_0\n  - contourpy=1.3.0=py310h3788b33_2\n  - coverage=7.6.1=py310ha75aee5_1\n  - curl=8.10.1=hbbe4b11_0\n  - cycler=0.12.1=pyhd8ed1ab_0\n  - cytoolz=1.0.0=py310ha75aee5_1\n  - dask-expr=1.1.15=pyhd8ed1ab_0\n  - distarray=2.12.2=pyh050c7b8_4\n  - distlib=0.3.8=pyhd8ed1ab_0\n  - distributed=2024.9.1=pyhd8ed1ab_0\n  - docopt-ng=0.9.0=pyhd8ed1ab_0\n  - eccodes=2.38.0=h8bb6dbc_0\n  - esmf=8.6.1=nompi_h4441c20_3\n  - esmpy=8.6.1=pyhc1e730c_0\n  - exceptiongroup=1.2.2=pyhd8ed1ab_0\n  - execnet=2.1.1=pyhd8ed1ab_0\n  - fasteners=0.17.3=pyhd8ed1ab_0\n  - filelock=3.16.1=pyhd8ed1ab_0\n  - findlibs=0.0.5=pyhd8ed1ab_0\n  - flexcache=0.3=pyhd8ed1ab_0\n  - flexparser=0.3.1=pyhd8ed1ab_0\n  - fonttools=4.54.1=py310ha75aee5_0\n  - freeglut=3.2.2=ha6d2627_3\n  - freetype=2.12.1=h267a509_2\n  - freexl=2.0.0=h743c826_0\n  - frozenlist=1.4.1=py310ha75aee5_1\n  - fsspec=2024.9.0=pyhff2d567_0\n  - future=1.0.0=pyhd8ed1ab_0\n  - g2clib=1.9.0=ha770c72_1\n  - geos=3.13.0=h5888daf_0\n  - geotiff=1.7.3=h77b800c_3\n  - gflags=2.2.2=h5888daf_1005\n  - giflib=5.2.2=hd590300_0\n  - glog=0.7.1=hbabe93e_0\n  - h2=4.1.0=pyhd8ed1ab_0\n  - h5netcdf=1.4.0=pyhd8ed1ab_0\n  - h5py=3.11.0=nompi_py310hf054cd7_102\n  - hdf4=4.2.15=h2a13503_7\n  - hdf5=1.14.3=nompi_hdf9ad27_105\n  - hpack=4.0.0=pyh9f0ad1d_0\n  - hyperframe=6.0.1=pyhd8ed1ab_0\n  - hypothesis=6.114.0=pyha770c72_0\n  - icu=75.1=he02047a_0\n  - identify=2.6.1=pyhd8ed1ab_0\n  - idna=3.10=pyhd8ed1ab_0\n  - importlib-metadata=8.5.0=pyha770c72_0\n  - importlib-resources=6.4.5=pyhd8ed1ab_0\n  - importlib_metadata=8.5.0=hd8ed1ab_0\n  - importlib_resources=6.4.5=pyhd8ed1ab_0\n  - iniconfig=2.0.0=pyhd8ed1ab_0\n  - iris=3.10.0=pyha770c72_1\n  - jasper=4.2.4=h536e39c_0\n  - jinja2=3.1.4=pyhd8ed1ab_0\n  - jmespath=1.0.1=pyhd8ed1ab_0\n  - json-c=0.18=h6688a6e_0\n  - jsonschema=4.23.0=pyhd8ed1ab_0\n  - jsonschema-specifications=2024.10.1=pyhd8ed1ab_0\n  - jupyter_core=5.7.2=pyh31011fe_1\n  - keyutils=1.6.1=h166bdaf_0\n  - kiwisolver=1.4.7=py310h3788b33_0\n  - krb5=1.21.3=h659f571_0\n  - lazy-object-proxy=1.10.0=py310h2372a71_0\n  - lcms2=2.16=hb7c19ff_0\n  - ld_impl_linux-64=2.43=h712a8e2_1\n  - lerc=4.0.0=h27087fc_0\n  - libabseil=20240722.0=cxx17_h5888daf_1\n  - libaec=1.1.3=h59595ed_0\n  - libarchive=3.7.4=hfca40fe_0\n  - libarrow=17.0.0=h364f349_19_cpu\n  - libarrow-acero=17.0.0=h5888daf_19_cpu\n  - libarrow-dataset=17.0.0=h5888daf_19_cpu\n  - libarrow-substrait=17.0.0=he882d9a_19_cpu\n  - libblas=3.9.0=24_linux64_openblas\n  - libbrotlicommon=1.1.0=hb9d3cd8_2\n  - libbrotlidec=1.1.0=hb9d3cd8_2\n  - libbrotlienc=1.1.0=hb9d3cd8_2\n  - libcblas=3.9.0=24_linux64_openblas\n  - libcdms=3.1.2=h0cec689_129\n  - libcf=1.0.3=py310h1588dd5_117\n  - libcrc32c=1.1.2=h9c3ff4c_0\n  - libcurl=8.10.1=hbbe4b11_0\n  - libdeflate=1.22=hb9d3cd8_0\n  - libedit=3.1.20191231=he28a2e2_2\n  - libev=4.33=hd590300_2\n  - libevent=2.1.12=hf998b51_1\n  - libexpat=2.6.3=h5888daf_0\n  - libffi=3.4.2=h7f98852_5\n  - libgcc=14.1.0=h77fa898_1\n  - libgcc-ng=14.1.0=h69a702a_1\n  - libgdal-core=3.9.2=hd5b9bfb_7\n  - libgfortran=14.1.0=h69a702a_1\n  - libgfortran-ng=14.1.0=h69a702a_1\n  - libgfortran5=14.1.0=hc5f4f2c_1\n  - libglu=9.0.0=ha6d2627_1004\n  - libgomp=14.1.0=h77fa898_1\n  - libgoogle-cloud=2.29.0=h438788a_1\n  - libgoogle-cloud-storage=2.29.0=h0121fbd_1\n  - libgrpc=1.65.5=hf5c653b_0\n  - libiconv=1.17=hd590300_2\n  - libjpeg-turbo=3.0.0=hd590300_1\n  - libkml=1.3.0=hf539b9f_1021\n  - liblapack=3.9.0=24_linux64_openblas\n  - libllvm14=14.0.6=hcd5def8_4\n  - libnetcdf=4.9.2=nompi_h135f659_114\n  - libnghttp2=1.58.0=h47da74e_1\n  - libnsl=2.0.1=hd590300_0\n  - libopenblas=0.3.27=pthreads_hac2b453_1\n  - libparquet=17.0.0=h6bd9018_19_cpu\n  - libpng=1.6.44=hadc24fc_0\n  - libprotobuf=5.27.5=h5b01275_2\n  - libre2-11=2023.11.01=hbbce691_0\n  - librttopo=1.1.0=h97f6797_17\n  - libspatialite=5.1.0=h1b4f908_11\n  - libsqlite=3.46.1=hadc24fc_0\n  - libssh2=1.11.0=h0841786_0\n  - libstdcxx=14.1.0=hc0a3c3a_1\n  - libstdcxx-ng=14.1.0=h4852527_1\n  - libthrift=0.21.0=h0e7cc3e_0\n  - libtiff=4.7.0=he137b08_1\n  - libudunits2=2.2.28=h40f5838_3\n  - libutf8proc=2.8.0=h166bdaf_0\n  - libuuid=2.38.1=h0b41bf4_0\n  - libwebp-base=1.4.0=hd590300_0\n  - libxcb=1.17.0=h8a09558_0\n  - libxcrypt=4.4.36=hd590300_1\n  - libxml2=2.12.7=he7c6b58_4\n  - libxslt=1.1.39=h76b75d6_0\n  - libzip=1.11.1=hf83b1b0_0\n  - libzlib=1.3.1=hb9d3cd8_2\n  - llvmlite=0.43.0=py310h1a6248f_1\n  - locket=1.0.0=pyhd8ed1ab_0\n  - lxml=5.3.0=py310h6ee67d5_1\n  - lz4=4.3.3=py310hb259640_1\n  - lz4-c=1.9.4=hcb278e6_0\n  - lzo=2.10=hd590300_1001\n  - markupsafe=3.0.1=py310h89163eb_1\n  - matplotlib-base=3.9.2=py310h68603db_1\n  - minizip=4.0.7=h401b404_0\n  - msgpack-python=1.1.0=py310h3788b33_0\n  - multidict=6.1.0=py310ha75aee5_0\n  - munkres=1.1.4=pyh9f0ad1d_0\n  - nbformat=5.10.4=pyhd8ed1ab_0\n  - nc-time-axis=1.4.1=pyhd8ed1ab_0\n  - nceplibs-g2c=1.9.0=ha39ef1c_1\n  - ncurses=6.5=he02047a_1\n  - netcdf-fortran=4.6.1=nompi_h22f9119_106\n  - netcdf4=1.7.1=nompi_py310h9f0ad05_102\n  - nodeenv=1.9.1=pyhd8ed1ab_0\n  - nomkl=1.0=h5ca1d4c_0\n  - numba=0.60.0=py310h5dc88bb_0\n  - numcodecs=0.13.0=py310h0cd1892_0\n  - numexpr=2.10.0=py310h3ea09b0_100\n  - openblas=0.3.27=pthreads_h9eca1d5_1\n  - openjpeg=2.5.2=h488ebb8_0\n  - openssl=3.3.2=hb9d3cd8_0\n  - orc=2.0.2=h690cf93_1\n  - partd=1.4.2=pyhd8ed1ab_0\n  - patsy=0.5.6=pyhd8ed1ab_0\n  - pcre2=10.44=hba22ea6_2\n  - pillow=10.4.0=py310he228d35_1\n  - pint=0.24.3=pyhd8ed1ab_0\n  - pip=24.2=pyh8b19718_1\n  - pkgutil-resolve-name=1.3.10=pyhd8ed1ab_1\n  - platformdirs=4.3.6=pyhd8ed1ab_0\n  - pluggy=1.5.0=pyhd8ed1ab_0\n  - pooch=1.8.2=pyhd8ed1ab_0\n  - pre-commit=4.0.1=pyha770c72_0\n  - proj=9.5.0=h12925eb_0\n  - pseudonetcdf=3.4.0=pyhd8ed1ab_0\n  - psutil=6.0.0=py310ha75aee5_1\n  - pthread-stubs=0.4=hb9d3cd8_1002\n  - pyarrow=17.0.0=py310hb7f781d_1\n  - pyarrow-core=17.0.0=py310h85d79f8_1_cpu\n  - pyarrow-hotfix=0.6=pyhd8ed1ab_0\n  - pycparser=2.22=pyhd8ed1ab_0\n  - pydap=3.5=pyhd8ed1ab_0\n  - pyparsing=3.1.4=pyhd8ed1ab_0\n  - pyproj=3.7.0=py310h2e9f774_0\n  - pyshp=2.3.1=pyhd8ed1ab_0\n  - pysocks=1.7.1=pyha2e5f31_6\n  - pytest-cov=5.0.0=pyhd8ed1ab_0\n  - pytest-env=1.1.5=pyhd8ed1ab_0\n  - pytest-xdist=3.6.1=pyhd8ed1ab_0\n  - python=3.10.15=h4a871b0_1_cpython\n  - python-eccodes=2.37.0=py310hf462985_0\n  - python-fastjsonschema=2.20.0=pyhd8ed1ab_0\n  - python-tzdata=2024.2=pyhd8ed1ab_0\n  - python-xxhash=3.5.0=py310ha75aee5_1\n  - python_abi=3.10=5_cp310\n  - pyyaml=6.0.2=py310ha75aee5_1\n  - qhull=2020.2=h434a139_5\n  - rasterio=1.4.1=py310hf6c6cbe_0\n  - re2=2023.11.01=h77b4e00_0\n  - readline=8.2=h8228510_1\n  - referencing=0.35.1=pyhd8ed1ab_0\n  - requests=2.32.3=pyhd8ed1ab_0\n  - rpds-py=0.20.0=py310h505e2c1_1\n  - s2n=1.5.4=h1380c3d_0\n  - s3transfer=0.10.3=pyhd8ed1ab_0\n  - seaborn=0.13.2=hd8ed1ab_2\n  - seaborn-base=0.13.2=pyhd8ed1ab_2\n  - shapely=2.0.6=py310had3dfd6_2\n  - six=1.16.0=pyh6c4a22f_0\n  - snappy=1.2.1=ha2e4443_0\n  - snuggs=1.4.7=pyhd8ed1ab_1\n  - sortedcontainers=2.4.0=pyhd8ed1ab_0\n  - soupsieve=2.5=pyhd8ed1ab_1\n  - sparse=0.15.4=pyh267e887_1\n  - sqlite=3.46.1=h9eae976_0\n  - statsmodels=0.14.4=py310hf462985_0\n  - tblib=3.0.0=pyhd8ed1ab_0\n  - tk=8.6.13=noxft_h4845f30_101\n  - toml=0.10.2=pyhd8ed1ab_0\n  - tomli=2.0.2=pyhd8ed1ab_0\n  - toolz=1.0.0=pyhd8ed1ab_0\n  - tornado=6.4.1=py310ha75aee5_1\n  - traitlets=5.14.3=pyhd8ed1ab_0\n  - typing-extensions=4.12.2=hd8ed1ab_0\n  - typing_extensions=4.12.2=pyha770c72_0\n  - tzdata=2024b=hc8b5060_0\n  - udunits2=2.2.28=h40f5838_3\n  - ukkonen=1.0.1=py310h3788b33_5\n  - unicodedata2=15.1.0=py310h2372a71_0\n  - uriparser=0.9.8=hac33072_0\n  - urllib3=2.2.3=pyhd8ed1ab_0\n  - virtualenv=20.26.6=pyhd8ed1ab_0\n  - webob=1.8.8=pyhd8ed1ab_0\n  - wheel=0.44.0=pyhd8ed1ab_0\n  - wrapt=1.16.0=py310ha75aee5_1\n  - xerces-c=3.2.5=h988505b_2\n  - xorg-libx11=1.8.10=h4f16b4b_0\n  - xorg-libxau=1.0.11=hb9d3cd8_1\n  - xorg-libxdmcp=1.1.5=hb9d3cd8_0\n  - xorg-libxext=1.3.6=hb9d3cd8_0\n  - xorg-libxfixes=6.0.1=hb9d3cd8_0\n  - xorg-libxi=1.8.2=hb9d3cd8_0\n  - xorg-xextproto=7.3.0=hb9d3cd8_1004\n  - xorg-xorgproto=2024.1=hb9d3cd8_1\n  - xxhash=0.8.2=hd590300_0\n  - xyzservices=2024.9.0=pyhd8ed1ab_0\n  - xz=5.2.6=h166bdaf_0\n  - yaml=0.2.5=h7f98852_2\n  - yarl=1.13.1=py310ha75aee5_0\n  - zarr=2.18.3=pyhd8ed1ab_0\n  - zict=3.0.0=pyhd8ed1ab_0\n  - zipp=3.20.2=pyhd8ed1ab_0\n  - zlib=1.3.1=hb9d3cd8_2\n  - zstandard=0.23.0=py310ha39cb0e_1\n  - zstd=1.5.6=ha6fb4c9_0\n  - pip:\n      - dask==2022.8.1\n      - numbagg==0.8.2\n      - numpy==1.23.0\n      - packaging==23.1\n      - pandas==1.5.3\n      - pytest==7.4.0\n      - python-dateutil==2.8.2\n      - pytz==2023.3\n      - scipy==1.11.1\n      - setuptools==68.0.0\nprefix: /opt/miniconda3/envs/testbed",
    "pydata__xarray-4094": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=conda_forge\n  - _openmp_mutex=4.5=2_gnu\n  - affine=2.4.0=pyhd8ed1ab_0\n  - aiobotocore=2.15.1=pyhd8ed1ab_0\n  - aiohappyeyeballs=2.4.3=pyhd8ed1ab_0\n  - aiohttp=3.10.9=py310ha75aee5_0\n  - aioitertools=0.12.0=pyhd8ed1ab_0\n  - aiosignal=1.3.1=pyhd8ed1ab_0\n  - antlr-python-runtime=4.11.1=pyhd8ed1ab_0\n  - appdirs=1.4.4=pyh9f0ad1d_0\n  - asciitree=0.3.3=py_2\n  - async-timeout=4.0.3=pyhd8ed1ab_0\n  - attrs=24.2.0=pyh71513ae_0\n  - aws-c-auth=0.7.31=h57bd9a3_0\n  - aws-c-cal=0.7.4=hfd43aa1_1\n  - aws-c-common=0.9.28=hb9d3cd8_0\n  - aws-c-compression=0.2.19=h756ea98_1\n  - aws-c-event-stream=0.4.3=h29ce20c_2\n  - aws-c-http=0.8.10=h5e77a74_0\n  - aws-c-io=0.14.18=h4e6ae90_11\n  - aws-c-mqtt=0.10.7=h02abb05_0\n  - aws-c-s3=0.6.6=h834ce55_0\n  - aws-c-sdkutils=0.1.19=h756ea98_3\n  - aws-checksums=0.1.20=h756ea98_0\n  - aws-crt-cpp=0.28.3=h3e6eb3e_6\n  - aws-sdk-cpp=1.11.407=h9f1560d_0\n  - azure-core-cpp=1.13.0=h935415a_0\n  - azure-identity-cpp=1.9.0=hd126650_0\n  - azure-storage-blobs-cpp=12.13.0=h1d30c4a_0\n  - azure-storage-common-cpp=12.8.0=ha3822c6_0\n  - azure-storage-files-datalake-cpp=12.12.0=h0f25b8a_0\n  - backports.zoneinfo=0.2.1=py310hff52083_9\n  - beautifulsoup4=4.12.3=pyha770c72_0\n  - blosc=1.21.6=hef167b5_0\n  - bokeh=3.5.2=pyhd8ed1ab_0\n  - boto3=1.35.23=pyhd8ed1ab_0\n  - botocore=1.35.23=pyge310_1234567_0\n  - bottleneck=1.4.0=py310hf462985_2\n  - brotli=1.1.0=hb9d3cd8_2\n  - brotli-bin=1.1.0=hb9d3cd8_2\n  - brotli-python=1.1.0=py310hf71b8c6_2\n  - bzip2=1.0.8=h4bc722e_7\n  - c-ares=1.33.1=heb4867d_0\n  - ca-certificates=2024.8.30=hbcca054_0\n  - cached-property=1.5.2=hd8ed1ab_1\n  - cached_property=1.5.2=pyha770c72_1\n  - cartopy=0.24.0=py310h5eaa309_0\n  - cdat_info=8.2.1=pyhd8ed1ab_2\n  - cdms2=3.1.5=py310h366d46e_22\n  - cdtime=3.1.4=py310h7a088e3_13\n  - certifi=2024.8.30=pyhd8ed1ab_0\n  - cf-units=3.2.0=py310hf462985_6\n  - cffi=1.17.1=py310h8deb56e_0\n  - cfgrib=0.9.14.1=pyhd8ed1ab_0\n  - cfgv=3.3.1=pyhd8ed1ab_0\n  - cftime=1.6.4=py310hf462985_1\n  - charset-normalizer=3.4.0=pyhd8ed1ab_0\n  - click=8.1.7=unix_pyh707e725_0\n  - click-plugins=1.1.1=py_0\n  - cligj=0.7.2=pyhd8ed1ab_1\n  - cloudpickle=3.0.0=pyhd8ed1ab_0\n  - colorama=0.4.6=pyhd8ed1ab_0\n  - contourpy=1.3.0=py310h3788b33_2\n  - coverage=7.6.1=py310ha75aee5_1\n  - curl=8.10.1=hbbe4b11_0\n  - cycler=0.12.1=pyhd8ed1ab_0\n  - cytoolz=1.0.0=py310ha75aee5_1\n  - dask-expr=1.1.15=pyhd8ed1ab_0\n  - distarray=2.12.2=pyh050c7b8_4\n  - distlib=0.3.8=pyhd8ed1ab_0\n  - distributed=2024.9.1=pyhd8ed1ab_0\n  - docopt-ng=0.9.0=pyhd8ed1ab_0\n  - eccodes=2.38.0=h8bb6dbc_0\n  - esmf=8.6.1=nompi_h4441c20_3\n  - esmpy=8.6.1=pyhc1e730c_0\n  - exceptiongroup=1.2.2=pyhd8ed1ab_0\n  - execnet=2.1.1=pyhd8ed1ab_0\n  - fasteners=0.17.3=pyhd8ed1ab_0\n  - filelock=3.16.1=pyhd8ed1ab_0\n  - findlibs=0.0.5=pyhd8ed1ab_0\n  - flexcache=0.3=pyhd8ed1ab_0\n  - flexparser=0.3.1=pyhd8ed1ab_0\n  - fonttools=4.54.1=py310ha75aee5_0\n  - freeglut=3.2.2=ha6d2627_3\n  - freetype=2.12.1=h267a509_2\n  - freexl=2.0.0=h743c826_0\n  - frozenlist=1.4.1=py310ha75aee5_1\n  - fsspec=2024.9.0=pyhff2d567_0\n  - future=1.0.0=pyhd8ed1ab_0\n  - g2clib=1.9.0=ha770c72_1\n  - geos=3.13.0=h5888daf_0\n  - geotiff=1.7.3=h77b800c_3\n  - gflags=2.2.2=h5888daf_1005\n  - giflib=5.2.2=hd590300_0\n  - glog=0.7.1=hbabe93e_0\n  - h2=4.1.0=pyhd8ed1ab_0\n  - h5netcdf=1.4.0=pyhd8ed1ab_0\n  - h5py=3.11.0=nompi_py310hf054cd7_102\n  - hdf4=4.2.15=h2a13503_7\n  - hdf5=1.14.3=nompi_hdf9ad27_105\n  - hpack=4.0.0=pyh9f0ad1d_0\n  - hyperframe=6.0.1=pyhd8ed1ab_0\n  - hypothesis=6.114.0=pyha770c72_0\n  - icu=75.1=he02047a_0\n  - identify=2.6.1=pyhd8ed1ab_0\n  - idna=3.10=pyhd8ed1ab_0\n  - importlib-metadata=8.5.0=pyha770c72_0\n  - importlib-resources=6.4.5=pyhd8ed1ab_0\n  - importlib_metadata=8.5.0=hd8ed1ab_0\n  - importlib_resources=6.4.5=pyhd8ed1ab_0\n  - iniconfig=2.0.0=pyhd8ed1ab_0\n  - iris=3.10.0=pyha770c72_1\n  - jasper=4.2.4=h536e39c_0\n  - jinja2=3.1.4=pyhd8ed1ab_0\n  - jmespath=1.0.1=pyhd8ed1ab_0\n  - json-c=0.18=h6688a6e_0\n  - jsonschema=4.23.0=pyhd8ed1ab_0\n  - jsonschema-specifications=2024.10.1=pyhd8ed1ab_0\n  - jupyter_core=5.7.2=pyh31011fe_1\n  - keyutils=1.6.1=h166bdaf_0\n  - kiwisolver=1.4.7=py310h3788b33_0\n  - krb5=1.21.3=h659f571_0\n  - lazy-object-proxy=1.10.0=py310h2372a71_0\n  - lcms2=2.16=hb7c19ff_0\n  - ld_impl_linux-64=2.43=h712a8e2_1\n  - lerc=4.0.0=h27087fc_0\n  - libabseil=20240722.0=cxx17_h5888daf_1\n  - libaec=1.1.3=h59595ed_0\n  - libarchive=3.7.4=hfca40fe_0\n  - libarrow=17.0.0=h364f349_19_cpu\n  - libarrow-acero=17.0.0=h5888daf_19_cpu\n  - libarrow-dataset=17.0.0=h5888daf_19_cpu\n  - libarrow-substrait=17.0.0=he882d9a_19_cpu\n  - libblas=3.9.0=24_linux64_openblas\n  - libbrotlicommon=1.1.0=hb9d3cd8_2\n  - libbrotlidec=1.1.0=hb9d3cd8_2\n  - libbrotlienc=1.1.0=hb9d3cd8_2\n  - libcblas=3.9.0=24_linux64_openblas\n  - libcdms=3.1.2=h0cec689_129\n  - libcf=1.0.3=py310h1588dd5_117\n  - libcrc32c=1.1.2=h9c3ff4c_0\n  - libcurl=8.10.1=hbbe4b11_0\n  - libdeflate=1.22=hb9d3cd8_0\n  - libedit=3.1.20191231=he28a2e2_2\n  - libev=4.33=hd590300_2\n  - libevent=2.1.12=hf998b51_1\n  - libexpat=2.6.3=h5888daf_0\n  - libffi=3.4.2=h7f98852_5\n  - libgcc=14.1.0=h77fa898_1\n  - libgcc-ng=14.1.0=h69a702a_1\n  - libgdal-core=3.9.2=hd5b9bfb_7\n  - libgfortran=14.1.0=h69a702a_1\n  - libgfortran-ng=14.1.0=h69a702a_1\n  - libgfortran5=14.1.0=hc5f4f2c_1\n  - libglu=9.0.0=ha6d2627_1004\n  - libgomp=14.1.0=h77fa898_1\n  - libgoogle-cloud=2.29.0=h438788a_1\n  - libgoogle-cloud-storage=2.29.0=h0121fbd_1\n  - libgrpc=1.65.5=hf5c653b_0\n  - libiconv=1.17=hd590300_2\n  - libjpeg-turbo=3.0.0=hd590300_1\n  - libkml=1.3.0=hf539b9f_1021\n  - liblapack=3.9.0=24_linux64_openblas\n  - libllvm14=14.0.6=hcd5def8_4\n  - libnetcdf=4.9.2=nompi_h135f659_114\n  - libnghttp2=1.58.0=h47da74e_1\n  - libnsl=2.0.1=hd590300_0\n  - libopenblas=0.3.27=pthreads_hac2b453_1\n  - libparquet=17.0.0=h6bd9018_19_cpu\n  - libpng=1.6.44=hadc24fc_0\n  - libprotobuf=5.27.5=h5b01275_2\n  - libre2-11=2023.11.01=hbbce691_0\n  - librttopo=1.1.0=h97f6797_17\n  - libspatialite=5.1.0=h1b4f908_11\n  - libsqlite=3.46.1=hadc24fc_0\n  - libssh2=1.11.0=h0841786_0\n  - libstdcxx=14.1.0=hc0a3c3a_1\n  - libstdcxx-ng=14.1.0=h4852527_1\n  - libthrift=0.21.0=h0e7cc3e_0\n  - libtiff=4.7.0=he137b08_1\n  - libudunits2=2.2.28=h40f5838_3\n  - libutf8proc=2.8.0=h166bdaf_0\n  - libuuid=2.38.1=h0b41bf4_0\n  - libwebp-base=1.4.0=hd590300_0\n  - libxcb=1.17.0=h8a09558_0\n  - libxcrypt=4.4.36=hd590300_1\n  - libxml2=2.12.7=he7c6b58_4\n  - libxslt=1.1.39=h76b75d6_0\n  - libzip=1.11.1=hf83b1b0_0\n  - libzlib=1.3.1=hb9d3cd8_2\n  - llvmlite=0.43.0=py310h1a6248f_1\n  - locket=1.0.0=pyhd8ed1ab_0\n  - lxml=5.3.0=py310h6ee67d5_1\n  - lz4=4.3.3=py310hb259640_1\n  - lz4-c=1.9.4=hcb278e6_0\n  - lzo=2.10=hd590300_1001\n  - markupsafe=3.0.1=py310h89163eb_1\n  - matplotlib-base=3.9.2=py310h68603db_1\n  - minizip=4.0.7=h401b404_0\n  - msgpack-python=1.1.0=py310h3788b33_0\n  - multidict=6.1.0=py310ha75aee5_0\n  - munkres=1.1.4=pyh9f0ad1d_0\n  - nbformat=5.10.4=pyhd8ed1ab_0\n  - nc-time-axis=1.4.1=pyhd8ed1ab_0\n  - nceplibs-g2c=1.9.0=ha39ef1c_1\n  - ncurses=6.5=he02047a_1\n  - netcdf-fortran=4.6.1=nompi_h22f9119_106\n  - netcdf4=1.7.1=nompi_py310h9f0ad05_102\n  - nodeenv=1.9.1=pyhd8ed1ab_0\n  - nomkl=1.0=h5ca1d4c_0\n  - numba=0.60.0=py310h5dc88bb_0\n  - numcodecs=0.13.0=py310h0cd1892_0\n  - numexpr=2.10.0=py310h3ea09b0_100\n  - openblas=0.3.27=pthreads_h9eca1d5_1\n  - openjpeg=2.5.2=h488ebb8_0\n  - openssl=3.3.2=hb9d3cd8_0\n  - orc=2.0.2=h690cf93_1\n  - partd=1.4.2=pyhd8ed1ab_0\n  - patsy=0.5.6=pyhd8ed1ab_0\n  - pcre2=10.44=hba22ea6_2\n  - pillow=10.4.0=py310he228d35_1\n  - pint=0.24.3=pyhd8ed1ab_0\n  - pip=24.2=pyh8b19718_1\n  - pkgutil-resolve-name=1.3.10=pyhd8ed1ab_1\n  - platformdirs=4.3.6=pyhd8ed1ab_0\n  - pluggy=1.5.0=pyhd8ed1ab_0\n  - pooch=1.8.2=pyhd8ed1ab_0\n  - pre-commit=4.0.1=pyha770c72_0\n  - proj=9.5.0=h12925eb_0\n  - pseudonetcdf=3.4.0=pyhd8ed1ab_0\n  - psutil=6.0.0=py310ha75aee5_1\n  - pthread-stubs=0.4=hb9d3cd8_1002\n  - pyarrow=17.0.0=py310hb7f781d_1\n  - pyarrow-core=17.0.0=py310h85d79f8_1_cpu\n  - pyarrow-hotfix=0.6=pyhd8ed1ab_0\n  - pycparser=2.22=pyhd8ed1ab_0\n  - pydap=3.5=pyhd8ed1ab_0\n  - pyparsing=3.1.4=pyhd8ed1ab_0\n  - pyproj=3.7.0=py310h2e9f774_0\n  - pyshp=2.3.1=pyhd8ed1ab_0\n  - pysocks=1.7.1=pyha2e5f31_6\n  - pytest-cov=5.0.0=pyhd8ed1ab_0\n  - pytest-env=1.1.5=pyhd8ed1ab_0\n  - pytest-xdist=3.6.1=pyhd8ed1ab_0\n  - python=3.10.15=h4a871b0_1_cpython\n  - python-eccodes=2.37.0=py310hf462985_0\n  - python-fastjsonschema=2.20.0=pyhd8ed1ab_0\n  - python-tzdata=2024.2=pyhd8ed1ab_0\n  - python-xxhash=3.5.0=py310ha75aee5_1\n  - python_abi=3.10=5_cp310\n  - pyyaml=6.0.2=py310ha75aee5_1\n  - qhull=2020.2=h434a139_5\n  - rasterio=1.4.1=py310hf6c6cbe_0\n  - re2=2023.11.01=h77b4e00_0\n  - readline=8.2=h8228510_1\n  - referencing=0.35.1=pyhd8ed1ab_0\n  - requests=2.32.3=pyhd8ed1ab_0\n  - rpds-py=0.20.0=py310h505e2c1_1\n  - s2n=1.5.4=h1380c3d_0\n  - s3transfer=0.10.3=pyhd8ed1ab_0\n  - seaborn=0.13.2=hd8ed1ab_2\n  - seaborn-base=0.13.2=pyhd8ed1ab_2\n  - shapely=2.0.6=py310had3dfd6_2\n  - six=1.16.0=pyh6c4a22f_0\n  - snappy=1.2.1=ha2e4443_0\n  - snuggs=1.4.7=pyhd8ed1ab_1\n  - sortedcontainers=2.4.0=pyhd8ed1ab_0\n  - soupsieve=2.5=pyhd8ed1ab_1\n  - sparse=0.15.4=pyh267e887_1\n  - sqlite=3.46.1=h9eae976_0\n  - statsmodels=0.14.4=py310hf462985_0\n  - tblib=3.0.0=pyhd8ed1ab_0\n  - tk=8.6.13=noxft_h4845f30_101\n  - toml=0.10.2=pyhd8ed1ab_0\n  - tomli=2.0.2=pyhd8ed1ab_0\n  - toolz=1.0.0=pyhd8ed1ab_0\n  - tornado=6.4.1=py310ha75aee5_1\n  - traitlets=5.14.3=pyhd8ed1ab_0\n  - typing-extensions=4.12.2=hd8ed1ab_0\n  - typing_extensions=4.12.2=pyha770c72_0\n  - tzdata=2024b=hc8b5060_0\n  - udunits2=2.2.28=h40f5838_3\n  - ukkonen=1.0.1=py310h3788b33_5\n  - unicodedata2=15.1.0=py310h2372a71_0\n  - uriparser=0.9.8=hac33072_0\n  - urllib3=2.2.3=pyhd8ed1ab_0\n  - virtualenv=20.26.6=pyhd8ed1ab_0\n  - webob=1.8.8=pyhd8ed1ab_0\n  - wheel=0.44.0=pyhd8ed1ab_0\n  - wrapt=1.16.0=py310ha75aee5_1\n  - xerces-c=3.2.5=h988505b_2\n  - xorg-libx11=1.8.10=h4f16b4b_0\n  - xorg-libxau=1.0.11=hb9d3cd8_1\n  - xorg-libxdmcp=1.1.5=hb9d3cd8_0\n  - xorg-libxext=1.3.6=hb9d3cd8_0\n  - xorg-libxfixes=6.0.1=hb9d3cd8_0\n  - xorg-libxi=1.8.2=hb9d3cd8_0\n  - xorg-xextproto=7.3.0=hb9d3cd8_1004\n  - xorg-xorgproto=2024.1=hb9d3cd8_1\n  - xxhash=0.8.2=hd590300_0\n  - xyzservices=2024.9.0=pyhd8ed1ab_0\n  - xz=5.2.6=h166bdaf_0\n  - yaml=0.2.5=h7f98852_2\n  - yarl=1.13.1=py310ha75aee5_0\n  - zarr=2.18.3=pyhd8ed1ab_0\n  - zict=3.0.0=pyhd8ed1ab_0\n  - zipp=3.20.2=pyhd8ed1ab_0\n  - zlib=1.3.1=hb9d3cd8_2\n  - zstandard=0.23.0=py310ha39cb0e_1\n  - zstd=1.5.6=ha6fb4c9_0\n  - pip:\n      - dask==2022.8.1\n      - numbagg==0.8.2\n      - numpy==1.23.0\n      - packaging==23.1\n      - pandas==1.5.3\n      - pytest==7.4.0\n      - python-dateutil==2.8.2\n      - pytz==2023.3\n      - scipy==1.11.1\n      - setuptools==68.0.0\nprefix: /opt/miniconda3/envs/testbed",
    "pydata__xarray-4695": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=conda_forge\n  - _openmp_mutex=4.5=2_gnu\n  - affine=2.4.0=pyhd8ed1ab_0\n  - aiobotocore=2.15.1=pyhd8ed1ab_0\n  - aiohappyeyeballs=2.4.3=pyhd8ed1ab_0\n  - aiohttp=3.10.9=py310ha75aee5_0\n  - aioitertools=0.12.0=pyhd8ed1ab_0\n  - aiosignal=1.3.1=pyhd8ed1ab_0\n  - antlr-python-runtime=4.11.1=pyhd8ed1ab_0\n  - appdirs=1.4.4=pyh9f0ad1d_0\n  - asciitree=0.3.3=py_2\n  - async-timeout=4.0.3=pyhd8ed1ab_0\n  - attrs=24.2.0=pyh71513ae_0\n  - aws-c-auth=0.7.31=h57bd9a3_0\n  - aws-c-cal=0.7.4=hfd43aa1_1\n  - aws-c-common=0.9.28=hb9d3cd8_0\n  - aws-c-compression=0.2.19=h756ea98_1\n  - aws-c-event-stream=0.4.3=h29ce20c_2\n  - aws-c-http=0.8.10=h5e77a74_0\n  - aws-c-io=0.14.18=h4e6ae90_11\n  - aws-c-mqtt=0.10.7=h02abb05_0\n  - aws-c-s3=0.6.6=h834ce55_0\n  - aws-c-sdkutils=0.1.19=h756ea98_3\n  - aws-checksums=0.1.20=h756ea98_0\n  - aws-crt-cpp=0.28.3=h3e6eb3e_6\n  - aws-sdk-cpp=1.11.407=h9f1560d_0\n  - azure-core-cpp=1.13.0=h935415a_0\n  - azure-identity-cpp=1.9.0=hd126650_0\n  - azure-storage-blobs-cpp=12.13.0=h1d30c4a_0\n  - azure-storage-common-cpp=12.8.0=ha3822c6_0\n  - azure-storage-files-datalake-cpp=12.12.0=h0f25b8a_0\n  - backports.zoneinfo=0.2.1=py310hff52083_9\n  - beautifulsoup4=4.12.3=pyha770c72_0\n  - blosc=1.21.6=hef167b5_0\n  - bokeh=3.5.2=pyhd8ed1ab_0\n  - boto3=1.35.23=pyhd8ed1ab_0\n  - botocore=1.35.23=pyge310_1234567_0\n  - bottleneck=1.4.0=py310hf462985_2\n  - brotli=1.1.0=hb9d3cd8_2\n  - brotli-bin=1.1.0=hb9d3cd8_2\n  - brotli-python=1.1.0=py310hf71b8c6_2\n  - bzip2=1.0.8=h4bc722e_7\n  - c-ares=1.33.1=heb4867d_0\n  - ca-certificates=2024.8.30=hbcca054_0\n  - cached-property=1.5.2=hd8ed1ab_1\n  - cached_property=1.5.2=pyha770c72_1\n  - cartopy=0.24.0=py310h5eaa309_0\n  - cdat_info=8.2.1=pyhd8ed1ab_2\n  - cdms2=3.1.5=py310h366d46e_22\n  - cdtime=3.1.4=py310h7a088e3_13\n  - certifi=2024.8.30=pyhd8ed1ab_0\n  - cf-units=3.2.0=py310hf462985_6\n  - cffi=1.17.1=py310h8deb56e_0\n  - cfgrib=0.9.14.1=pyhd8ed1ab_0\n  - cfgv=3.3.1=pyhd8ed1ab_0\n  - cftime=1.6.4=py310hf462985_1\n  - charset-normalizer=3.4.0=pyhd8ed1ab_0\n  - click=8.1.7=unix_pyh707e725_0\n  - click-plugins=1.1.1=py_0\n  - cligj=0.7.2=pyhd8ed1ab_1\n  - cloudpickle=3.0.0=pyhd8ed1ab_0\n  - colorama=0.4.6=pyhd8ed1ab_0\n  - contourpy=1.3.0=py310h3788b33_2\n  - coverage=7.6.1=py310ha75aee5_1\n  - curl=8.10.1=hbbe4b11_0\n  - cycler=0.12.1=pyhd8ed1ab_0\n  - cytoolz=1.0.0=py310ha75aee5_1\n  - dask-expr=1.1.15=pyhd8ed1ab_0\n  - distarray=2.12.2=pyh050c7b8_4\n  - distlib=0.3.8=pyhd8ed1ab_0\n  - distributed=2024.9.1=pyhd8ed1ab_0\n  - docopt-ng=0.9.0=pyhd8ed1ab_0\n  - eccodes=2.38.0=h8bb6dbc_0\n  - esmf=8.6.1=nompi_h4441c20_3\n  - esmpy=8.6.1=pyhc1e730c_0\n  - exceptiongroup=1.2.2=pyhd8ed1ab_0\n  - execnet=2.1.1=pyhd8ed1ab_0\n  - fasteners=0.17.3=pyhd8ed1ab_0\n  - filelock=3.16.1=pyhd8ed1ab_0\n  - findlibs=0.0.5=pyhd8ed1ab_0\n  - flexcache=0.3=pyhd8ed1ab_0\n  - flexparser=0.3.1=pyhd8ed1ab_0\n  - fonttools=4.54.1=py310ha75aee5_0\n  - freeglut=3.2.2=ha6d2627_3\n  - freetype=2.12.1=h267a509_2\n  - freexl=2.0.0=h743c826_0\n  - frozenlist=1.4.1=py310ha75aee5_1\n  - fsspec=2024.9.0=pyhff2d567_0\n  - future=1.0.0=pyhd8ed1ab_0\n  - g2clib=1.9.0=ha770c72_1\n  - geos=3.13.0=h5888daf_0\n  - geotiff=1.7.3=h77b800c_3\n  - gflags=2.2.2=h5888daf_1005\n  - giflib=5.2.2=hd590300_0\n  - glog=0.7.1=hbabe93e_0\n  - h2=4.1.0=pyhd8ed1ab_0\n  - h5netcdf=1.4.0=pyhd8ed1ab_0\n  - h5py=3.11.0=nompi_py310hf054cd7_102\n  - hdf4=4.2.15=h2a13503_7\n  - hdf5=1.14.3=nompi_hdf9ad27_105\n  - hpack=4.0.0=pyh9f0ad1d_0\n  - hyperframe=6.0.1=pyhd8ed1ab_0\n  - hypothesis=6.114.0=pyha770c72_0\n  - icu=75.1=he02047a_0\n  - identify=2.6.1=pyhd8ed1ab_0\n  - idna=3.10=pyhd8ed1ab_0\n  - importlib-metadata=8.5.0=pyha770c72_0\n  - importlib-resources=6.4.5=pyhd8ed1ab_0\n  - importlib_metadata=8.5.0=hd8ed1ab_0\n  - importlib_resources=6.4.5=pyhd8ed1ab_0\n  - iniconfig=2.0.0=pyhd8ed1ab_0\n  - iris=3.10.0=pyha770c72_1\n  - jasper=4.2.4=h536e39c_0\n  - jinja2=3.1.4=pyhd8ed1ab_0\n  - jmespath=1.0.1=pyhd8ed1ab_0\n  - json-c=0.18=h6688a6e_0\n  - jsonschema=4.23.0=pyhd8ed1ab_0\n  - jsonschema-specifications=2024.10.1=pyhd8ed1ab_0\n  - jupyter_core=5.7.2=pyh31011fe_1\n  - keyutils=1.6.1=h166bdaf_0\n  - kiwisolver=1.4.7=py310h3788b33_0\n  - krb5=1.21.3=h659f571_0\n  - lazy-object-proxy=1.10.0=py310h2372a71_0\n  - lcms2=2.16=hb7c19ff_0\n  - ld_impl_linux-64=2.43=h712a8e2_1\n  - lerc=4.0.0=h27087fc_0\n  - libabseil=20240722.0=cxx17_h5888daf_1\n  - libaec=1.1.3=h59595ed_0\n  - libarchive=3.7.4=hfca40fe_0\n  - libarrow=17.0.0=h364f349_19_cpu\n  - libarrow-acero=17.0.0=h5888daf_19_cpu\n  - libarrow-dataset=17.0.0=h5888daf_19_cpu\n  - libarrow-substrait=17.0.0=he882d9a_19_cpu\n  - libblas=3.9.0=24_linux64_openblas\n  - libbrotlicommon=1.1.0=hb9d3cd8_2\n  - libbrotlidec=1.1.0=hb9d3cd8_2\n  - libbrotlienc=1.1.0=hb9d3cd8_2\n  - libcblas=3.9.0=24_linux64_openblas\n  - libcdms=3.1.2=h0cec689_129\n  - libcf=1.0.3=py310h1588dd5_117\n  - libcrc32c=1.1.2=h9c3ff4c_0\n  - libcurl=8.10.1=hbbe4b11_0\n  - libdeflate=1.22=hb9d3cd8_0\n  - libedit=3.1.20191231=he28a2e2_2\n  - libev=4.33=hd590300_2\n  - libevent=2.1.12=hf998b51_1\n  - libexpat=2.6.3=h5888daf_0\n  - libffi=3.4.2=h7f98852_5\n  - libgcc=14.1.0=h77fa898_1\n  - libgcc-ng=14.1.0=h69a702a_1\n  - libgdal-core=3.9.2=hd5b9bfb_7\n  - libgfortran=14.1.0=h69a702a_1\n  - libgfortran-ng=14.1.0=h69a702a_1\n  - libgfortran5=14.1.0=hc5f4f2c_1\n  - libglu=9.0.0=ha6d2627_1004\n  - libgomp=14.1.0=h77fa898_1\n  - libgoogle-cloud=2.29.0=h438788a_1\n  - libgoogle-cloud-storage=2.29.0=h0121fbd_1\n  - libgrpc=1.65.5=hf5c653b_0\n  - libiconv=1.17=hd590300_2\n  - libjpeg-turbo=3.0.0=hd590300_1\n  - libkml=1.3.0=hf539b9f_1021\n  - liblapack=3.9.0=24_linux64_openblas\n  - libllvm14=14.0.6=hcd5def8_4\n  - libnetcdf=4.9.2=nompi_h135f659_114\n  - libnghttp2=1.58.0=h47da74e_1\n  - libnsl=2.0.1=hd590300_0\n  - libopenblas=0.3.27=pthreads_hac2b453_1\n  - libparquet=17.0.0=h6bd9018_19_cpu\n  - libpng=1.6.44=hadc24fc_0\n  - libprotobuf=5.27.5=h5b01275_2\n  - libre2-11=2023.11.01=hbbce691_0\n  - librttopo=1.1.0=h97f6797_17\n  - libspatialite=5.1.0=h1b4f908_11\n  - libsqlite=3.46.1=hadc24fc_0\n  - libssh2=1.11.0=h0841786_0\n  - libstdcxx=14.1.0=hc0a3c3a_1\n  - libstdcxx-ng=14.1.0=h4852527_1\n  - libthrift=0.21.0=h0e7cc3e_0\n  - libtiff=4.7.0=he137b08_1\n  - libudunits2=2.2.28=h40f5838_3\n  - libutf8proc=2.8.0=h166bdaf_0\n  - libuuid=2.38.1=h0b41bf4_0\n  - libwebp-base=1.4.0=hd590300_0\n  - libxcb=1.17.0=h8a09558_0\n  - libxcrypt=4.4.36=hd590300_1\n  - libxml2=2.12.7=he7c6b58_4\n  - libxslt=1.1.39=h76b75d6_0\n  - libzip=1.11.1=hf83b1b0_0\n  - libzlib=1.3.1=hb9d3cd8_2\n  - llvmlite=0.43.0=py310h1a6248f_1\n  - locket=1.0.0=pyhd8ed1ab_0\n  - lxml=5.3.0=py310h6ee67d5_1\n  - lz4=4.3.3=py310hb259640_1\n  - lz4-c=1.9.4=hcb278e6_0\n  - lzo=2.10=hd590300_1001\n  - markupsafe=3.0.1=py310h89163eb_1\n  - matplotlib-base=3.9.2=py310h68603db_1\n  - minizip=4.0.7=h401b404_0\n  - msgpack-python=1.1.0=py310h3788b33_0\n  - multidict=6.1.0=py310ha75aee5_0\n  - munkres=1.1.4=pyh9f0ad1d_0\n  - nbformat=5.10.4=pyhd8ed1ab_0\n  - nc-time-axis=1.4.1=pyhd8ed1ab_0\n  - nceplibs-g2c=1.9.0=ha39ef1c_1\n  - ncurses=6.5=he02047a_1\n  - netcdf-fortran=4.6.1=nompi_h22f9119_106\n  - netcdf4=1.7.1=nompi_py310h9f0ad05_102\n  - nodeenv=1.9.1=pyhd8ed1ab_0\n  - nomkl=1.0=h5ca1d4c_0\n  - numba=0.60.0=py310h5dc88bb_0\n  - numcodecs=0.13.0=py310h0cd1892_0\n  - numexpr=2.10.0=py310h3ea09b0_100\n  - openblas=0.3.27=pthreads_h9eca1d5_1\n  - openjpeg=2.5.2=h488ebb8_0\n  - openssl=3.3.2=hb9d3cd8_0\n  - orc=2.0.2=h690cf93_1\n  - partd=1.4.2=pyhd8ed1ab_0\n  - patsy=0.5.6=pyhd8ed1ab_0\n  - pcre2=10.44=hba22ea6_2\n  - pillow=10.4.0=py310he228d35_1\n  - pint=0.24.3=pyhd8ed1ab_0\n  - pip=24.2=pyh8b19718_1\n  - pkgutil-resolve-name=1.3.10=pyhd8ed1ab_1\n  - platformdirs=4.3.6=pyhd8ed1ab_0\n  - pluggy=1.5.0=pyhd8ed1ab_0\n  - pooch=1.8.2=pyhd8ed1ab_0\n  - pre-commit=4.0.1=pyha770c72_0\n  - proj=9.5.0=h12925eb_0\n  - pseudonetcdf=3.4.0=pyhd8ed1ab_0\n  - psutil=6.0.0=py310ha75aee5_1\n  - pthread-stubs=0.4=hb9d3cd8_1002\n  - pyarrow=17.0.0=py310hb7f781d_1\n  - pyarrow-core=17.0.0=py310h85d79f8_1_cpu\n  - pyarrow-hotfix=0.6=pyhd8ed1ab_0\n  - pycparser=2.22=pyhd8ed1ab_0\n  - pydap=3.5=pyhd8ed1ab_0\n  - pyparsing=3.1.4=pyhd8ed1ab_0\n  - pyproj=3.7.0=py310h2e9f774_0\n  - pyshp=2.3.1=pyhd8ed1ab_0\n  - pysocks=1.7.1=pyha2e5f31_6\n  - pytest-cov=5.0.0=pyhd8ed1ab_0\n  - pytest-env=1.1.5=pyhd8ed1ab_0\n  - pytest-xdist=3.6.1=pyhd8ed1ab_0\n  - python=3.10.15=h4a871b0_1_cpython\n  - python-eccodes=2.37.0=py310hf462985_0\n  - python-fastjsonschema=2.20.0=pyhd8ed1ab_0\n  - python-tzdata=2024.2=pyhd8ed1ab_0\n  - python-xxhash=3.5.0=py310ha75aee5_1\n  - python_abi=3.10=5_cp310\n  - pyyaml=6.0.2=py310ha75aee5_1\n  - qhull=2020.2=h434a139_5\n  - rasterio=1.4.1=py310hf6c6cbe_0\n  - re2=2023.11.01=h77b4e00_0\n  - readline=8.2=h8228510_1\n  - referencing=0.35.1=pyhd8ed1ab_0\n  - requests=2.32.3=pyhd8ed1ab_0\n  - rpds-py=0.20.0=py310h505e2c1_1\n  - s2n=1.5.4=h1380c3d_0\n  - s3transfer=0.10.3=pyhd8ed1ab_0\n  - seaborn=0.13.2=hd8ed1ab_2\n  - seaborn-base=0.13.2=pyhd8ed1ab_2\n  - shapely=2.0.6=py310had3dfd6_2\n  - six=1.16.0=pyh6c4a22f_0\n  - snappy=1.2.1=ha2e4443_0\n  - snuggs=1.4.7=pyhd8ed1ab_1\n  - sortedcontainers=2.4.0=pyhd8ed1ab_0\n  - soupsieve=2.5=pyhd8ed1ab_1\n  - sparse=0.15.4=pyh267e887_1\n  - sqlite=3.46.1=h9eae976_0\n  - statsmodels=0.14.4=py310hf462985_0\n  - tblib=3.0.0=pyhd8ed1ab_0\n  - tk=8.6.13=noxft_h4845f30_101\n  - toml=0.10.2=pyhd8ed1ab_0\n  - tomli=2.0.2=pyhd8ed1ab_0\n  - toolz=1.0.0=pyhd8ed1ab_0\n  - tornado=6.4.1=py310ha75aee5_1\n  - traitlets=5.14.3=pyhd8ed1ab_0\n  - typing-extensions=4.12.2=hd8ed1ab_0\n  - typing_extensions=4.12.2=pyha770c72_0\n  - tzdata=2024b=hc8b5060_0\n  - udunits2=2.2.28=h40f5838_3\n  - ukkonen=1.0.1=py310h3788b33_5\n  - unicodedata2=15.1.0=py310h2372a71_0\n  - uriparser=0.9.8=hac33072_0\n  - urllib3=2.2.3=pyhd8ed1ab_0\n  - virtualenv=20.26.6=pyhd8ed1ab_0\n  - webob=1.8.8=pyhd8ed1ab_0\n  - wheel=0.44.0=pyhd8ed1ab_0\n  - wrapt=1.16.0=py310ha75aee5_1\n  - xerces-c=3.2.5=h988505b_2\n  - xorg-libx11=1.8.10=h4f16b4b_0\n  - xorg-libxau=1.0.11=hb9d3cd8_1\n  - xorg-libxdmcp=1.1.5=hb9d3cd8_0\n  - xorg-libxext=1.3.6=hb9d3cd8_0\n  - xorg-libxfixes=6.0.1=hb9d3cd8_0\n  - xorg-libxi=1.8.2=hb9d3cd8_0\n  - xorg-xextproto=7.3.0=hb9d3cd8_1004\n  - xorg-xorgproto=2024.1=hb9d3cd8_1\n  - xxhash=0.8.2=hd590300_0\n  - xyzservices=2024.9.0=pyhd8ed1ab_0\n  - xz=5.2.6=h166bdaf_0\n  - yaml=0.2.5=h7f98852_2\n  - yarl=1.13.1=py310ha75aee5_0\n  - zarr=2.18.3=pyhd8ed1ab_0\n  - zict=3.0.0=pyhd8ed1ab_0\n  - zipp=3.20.2=pyhd8ed1ab_0\n  - zlib=1.3.1=hb9d3cd8_2\n  - zstandard=0.23.0=py310ha39cb0e_1\n  - zstd=1.5.6=ha6fb4c9_0\n  - pip:\n      - dask==2022.8.1\n      - numbagg==0.8.2\n      - numpy==1.23.0\n      - packaging==23.1\n      - pandas==1.5.3\n      - pytest==7.4.0\n      - python-dateutil==2.8.2\n      - pytz==2023.3\n      - scipy==1.11.1\n      - setuptools==68.0.0\nprefix: /opt/miniconda3/envs/testbed",
    "pydata__xarray-6721": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=conda_forge\n  - _openmp_mutex=4.5=2_gnu\n  - affine=2.4.0=pyhd8ed1ab_0\n  - aiobotocore=2.15.1=pyhd8ed1ab_0\n  - aiohappyeyeballs=2.4.3=pyhd8ed1ab_0\n  - aiohttp=3.10.10=py310h89163eb_0\n  - aioitertools=0.12.0=pyhd8ed1ab_0\n  - aiosignal=1.3.1=pyhd8ed1ab_0\n  - antlr-python-runtime=4.11.1=pyhd8ed1ab_0\n  - appdirs=1.4.4=pyh9f0ad1d_0\n  - asciitree=0.3.3=py_2\n  - async-timeout=4.0.3=pyhd8ed1ab_0\n  - attrs=24.2.0=pyh71513ae_0\n  - backports.zoneinfo=0.2.1=py310hff52083_9\n  - beautifulsoup4=4.12.3=pyha770c72_0\n  - blosc=1.21.6=hef167b5_0\n  - boto3=1.35.23=pyhd8ed1ab_0\n  - botocore=1.35.23=pyge310_1234567_0\n  - bottleneck=1.4.2=py310hf462985_0\n  - brotli=1.1.0=hb9d3cd8_2\n  - brotli-bin=1.1.0=hb9d3cd8_2\n  - brotli-python=1.1.0=py310hf71b8c6_2\n  - bzip2=1.0.8=h4bc722e_7\n  - c-ares=1.34.2=heb4867d_0\n  - ca-certificates=2024.8.30=hbcca054_0\n  - cached-property=1.5.2=hd8ed1ab_1\n  - cached_property=1.5.2=pyha770c72_1\n  - cartopy=0.24.0=py310h5eaa309_0\n  - cdat_info=8.2.1=pyhd8ed1ab_2\n  - cdms2=3.1.5=py310h366d46e_22\n  - cdtime=3.1.4=py310h7a088e3_13\n  - certifi=2024.8.30=pyhd8ed1ab_0\n  - cf-units=3.2.0=py310hf462985_6\n  - cffi=1.17.1=py310h8deb56e_0\n  - cfgrib=0.9.14.1=pyhd8ed1ab_0\n  - cfgv=3.3.1=pyhd8ed1ab_0\n  - cftime=1.6.4=py310hf462985_1\n  - charset-normalizer=3.4.0=pyhd8ed1ab_0\n  - click=8.1.7=unix_pyh707e725_0\n  - click-plugins=1.1.1=py_0\n  - cligj=0.7.2=pyhd8ed1ab_1\n  - cloudpickle=3.1.0=pyhd8ed1ab_1\n  - colorama=0.4.6=pyhd8ed1ab_0\n  - contourpy=1.3.0=py310h3788b33_2\n  - coverage=7.6.4=py310h89163eb_0\n  - curl=8.10.1=hbbe4b11_0\n  - cycler=0.12.1=pyhd8ed1ab_0\n  - cytoolz=1.0.0=py310ha75aee5_1\n  - distarray=2.12.2=pyh050c7b8_4\n  - distlib=0.3.9=pyhd8ed1ab_0\n  - distributed=2024.10.0=pyhd8ed1ab_0\n  - docopt-ng=0.9.0=pyhd8ed1ab_0\n  - eccodes=2.38.0=h8bb6dbc_0\n  - esmf=8.6.1=nompi_h4441c20_3\n  - esmpy=8.6.1=pyhc1e730c_0\n  - exceptiongroup=1.2.2=pyhd8ed1ab_0\n  - execnet=2.1.1=pyhd8ed1ab_0\n  - fasteners=0.17.3=pyhd8ed1ab_0\n  - filelock=3.16.1=pyhd8ed1ab_0\n  - findlibs=0.0.5=pyhd8ed1ab_0\n  - flexcache=0.3=pyhd8ed1ab_0\n  - flexparser=0.3.1=pyhd8ed1ab_0\n  - flox=0.9.12=pyhd8ed1ab_0\n  - fonttools=4.54.1=py310h89163eb_1\n  - freeglut=3.2.2=ha6d2627_3\n  - freetype=2.12.1=h267a509_2\n  - freexl=2.0.0=h743c826_0\n  - frozenlist=1.5.0=py310ha75aee5_0\n  - fsspec=2024.10.0=pyhff2d567_0\n  - future=1.0.0=pyhd8ed1ab_0\n  - g2clib=1.9.0=ha770c72_1\n  - geos=3.13.0=h5888daf_0\n  - geotiff=1.7.3=h77b800c_3\n  - giflib=5.2.2=hd590300_0\n  - h2=4.1.0=pyhd8ed1ab_0\n  - h5netcdf=1.4.0=pyhd8ed1ab_0\n  - h5py=3.12.1=nompi_py310h60e0fe6_102\n  - hdf4=4.2.15=h2a13503_7\n  - hdf5=1.14.3=nompi_hdf9ad27_105\n  - hpack=4.0.0=pyh9f0ad1d_0\n  - hyperframe=6.0.1=pyhd8ed1ab_0\n  - hypothesis=6.115.5=pyha770c72_0\n  - icu=75.1=he02047a_0\n  - identify=2.6.1=pyhd8ed1ab_0\n  - idna=3.10=pyhd8ed1ab_0\n  - importlib-metadata=8.5.0=pyha770c72_0\n  - importlib-resources=6.4.5=pyhd8ed1ab_0\n  - importlib_metadata=8.5.0=hd8ed1ab_0\n  - importlib_resources=6.4.5=pyhd8ed1ab_0\n  - iniconfig=2.0.0=pyhd8ed1ab_0\n  - iris=3.10.0=pyha770c72_1\n  - jasper=4.2.4=h536e39c_0\n  - jinja2=3.1.4=pyhd8ed1ab_0\n  - jmespath=1.0.1=pyhd8ed1ab_0\n  - json-c=0.18=h6688a6e_0\n  - jsonschema=4.23.0=pyhd8ed1ab_0\n  - jsonschema-specifications=2024.10.1=pyhd8ed1ab_0\n  - jupyter_core=5.7.2=pyh31011fe_1\n  - keyutils=1.6.1=h166bdaf_0\n  - kiwisolver=1.4.7=py310h3788b33_0\n  - krb5=1.21.3=h659f571_0\n  - lazy-object-proxy=1.10.0=py310h2372a71_0\n  - lcms2=2.16=hb7c19ff_0\n  - ld_impl_linux-64=2.43=h712a8e2_2\n  - lerc=4.0.0=h27087fc_0\n  - libaec=1.1.3=h59595ed_0\n  - libarchive=3.7.4=hfca40fe_0\n  - libblas=3.9.0=25_linux64_openblas\n  - libbrotlicommon=1.1.0=hb9d3cd8_2\n  - libbrotlidec=1.1.0=hb9d3cd8_2\n  - libbrotlienc=1.1.0=hb9d3cd8_2\n  - libcblas=3.9.0=25_linux64_openblas\n  - libcdms=3.1.2=h0cec689_129\n  - libcf=1.0.3=py310h1588dd5_117\n  - libcurl=8.10.1=hbbe4b11_0\n  - libdeflate=1.22=hb9d3cd8_0\n  - libedit=3.1.20191231=he28a2e2_2\n  - libev=4.33=hd590300_2\n  - libexpat=2.6.3=h5888daf_0\n  - libffi=3.4.2=h7f98852_5\n  - libgcc=14.2.0=h77fa898_1\n  - libgcc-ng=14.2.0=h69a702a_1\n  - libgdal-core=3.9.2=hd5b9bfb_7\n  - libgfortran=14.2.0=h69a702a_1\n  - libgfortran-ng=14.2.0=h69a702a_1\n  - libgfortran5=14.2.0=hd5240d6_1\n  - libglu=9.0.0=ha6d2627_1004\n  - libgomp=14.2.0=h77fa898_1\n  - libiconv=1.17=hd590300_2\n  - libjpeg-turbo=3.0.0=hd590300_1\n  - libkml=1.3.0=hf539b9f_1021\n  - liblapack=3.9.0=25_linux64_openblas\n  - libllvm14=14.0.6=hcd5def8_4\n  - libnetcdf=4.9.2=nompi_h135f659_114\n  - libnghttp2=1.64.0=h161d5f1_0\n  - libnsl=2.0.1=hd590300_0\n  - libopenblas=0.3.28=pthreads_h94d23a6_0\n  - libpng=1.6.44=hadc24fc_0\n  - librttopo=1.1.0=h97f6797_17\n  - libspatialite=5.1.0=h1b4f908_11\n  - libsqlite=3.47.0=hadc24fc_0\n  - libssh2=1.11.0=h0841786_0\n  - libstdcxx=14.2.0=hc0a3c3a_1\n  - libstdcxx-ng=14.2.0=h4852527_1\n  - libtiff=4.7.0=he137b08_1\n  - libudunits2=2.2.28=h40f5838_3\n  - libuuid=2.38.1=h0b41bf4_0\n  - libwebp-base=1.4.0=hd590300_0\n  - libxcb=1.17.0=h8a09558_0\n  - libxcrypt=4.4.36=hd590300_1\n  - libxml2=2.12.7=he7c6b58_4\n  - libxslt=1.1.39=h76b75d6_0\n  - libzip=1.11.1=hf83b1b0_0\n  - libzlib=1.3.1=hb9d3cd8_2\n  - llvmlite=0.43.0=py310h1a6248f_1\n  - locket=1.0.0=pyhd8ed1ab_0\n  - lxml=5.3.0=py310h6ee67d5_1\n  - lz4-c=1.9.4=hcb278e6_0\n  - lzo=2.10=hd590300_1001\n  - markupsafe=3.0.2=py310h89163eb_0\n  - matplotlib-base=3.9.2=py310h68603db_1\n  - minizip=4.0.7=h401b404_0\n  - msgpack-python=1.1.0=py310h3788b33_0\n  - multidict=6.1.0=py310h89163eb_1\n  - munkres=1.1.4=pyh9f0ad1d_0\n  - nbformat=5.10.4=pyhd8ed1ab_0\n  - nc-time-axis=1.4.1=pyhd8ed1ab_0\n  - nceplibs-g2c=1.9.0=ha39ef1c_1\n  - ncurses=6.5=he02047a_1\n  - netcdf-fortran=4.6.1=nompi_h22f9119_106\n  - netcdf4=1.7.1=nompi_py310h9f0ad05_102\n  - nodeenv=1.9.1=pyhd8ed1ab_0\n  - nomkl=1.0=h5ca1d4c_0\n  - numba=0.60.0=py310h5dc88bb_0\n  - numcodecs=0.13.1=py310h5eaa309_0\n  - numexpr=2.10.1=py310hdb6e06b_103\n  - numpy_groupies=0.11.2=pyhd8ed1ab_0\n  - openblas=0.3.28=pthreads_hbcdf1e8_0\n  - openjpeg=2.5.2=h488ebb8_0\n  - openssl=3.3.2=hb9d3cd8_0\n  - partd=1.4.2=pyhd8ed1ab_0\n  - patsy=0.5.6=pyhd8ed1ab_0\n  - pcre2=10.44=hba22ea6_2\n  - pillow=11.0.0=py310hfeaa1f3_0\n  - pint=0.24.3=pyhd8ed1ab_0\n  - pip=24.2=pyh8b19718_1\n  - pkgutil-resolve-name=1.3.10=pyhd8ed1ab_1\n  - platformdirs=4.3.6=pyhd8ed1ab_0\n  - pluggy=1.5.0=pyhd8ed1ab_0\n  - pooch=1.8.2=pyhd8ed1ab_0\n  - pre-commit=4.0.1=pyha770c72_0\n  - proj=9.5.0=h12925eb_0\n  - propcache=0.2.0=py310ha75aee5_2\n  - pseudonetcdf=3.4.0=pyhd8ed1ab_0\n  - psutil=6.0.0=py310ha75aee5_2\n  - pthread-stubs=0.4=hb9d3cd8_1002\n  - pycparser=2.22=pyhd8ed1ab_0\n  - pydap=3.5=pyhd8ed1ab_0\n  - pyparsing=3.2.0=pyhd8ed1ab_1\n  - pyproj=3.7.0=py310h2e9f774_0\n  - pyshp=2.3.1=pyhd8ed1ab_0\n  - pysocks=1.7.1=pyha2e5f31_6\n  - pytest-cov=5.0.0=pyhd8ed1ab_0\n  - pytest-env=1.1.5=pyhd8ed1ab_0\n  - pytest-xdist=3.6.1=pyhd8ed1ab_0\n  - python=3.10.15=h4a871b0_2_cpython\n  - python-eccodes=2.37.0=py310hf462985_0\n  - python-fastjsonschema=2.20.0=pyhd8ed1ab_0\n  - python-tzdata=2024.2=pyhd8ed1ab_0\n  - python-xxhash=3.5.0=py310ha75aee5_1\n  - python_abi=3.10=5_cp310\n  - pyyaml=6.0.2=py310ha75aee5_1\n  - qhull=2020.2=h434a139_5\n  - rasterio=1.4.1=py310hf6c6cbe_0\n  - readline=8.2=h8228510_1\n  - referencing=0.35.1=pyhd8ed1ab_0\n  - requests=2.32.3=pyhd8ed1ab_0\n  - rpds-py=0.20.0=py310h505e2c1_1\n  - s3transfer=0.10.3=pyhd8ed1ab_0\n  - seaborn=0.13.2=hd8ed1ab_2\n  - seaborn-base=0.13.2=pyhd8ed1ab_2\n  - shapely=2.0.6=py310had3dfd6_2\n  - six=1.16.0=pyh6c4a22f_0\n  - snappy=1.2.1=ha2e4443_0\n  - snuggs=1.4.7=pyhd8ed1ab_1\n  - sortedcontainers=2.4.0=pyhd8ed1ab_0\n  - soupsieve=2.5=pyhd8ed1ab_1\n  - sparse=0.15.4=pyh267e887_1\n  - sqlite=3.47.0=h9eae976_0\n  - statsmodels=0.14.4=py310hf462985_0\n  - tblib=3.0.0=pyhd8ed1ab_0\n  - tk=8.6.13=noxft_h4845f30_101\n  - toml=0.10.2=pyhd8ed1ab_0\n  - tomli=2.0.2=pyhd8ed1ab_0\n  - toolz=1.0.0=pyhd8ed1ab_0\n  - tornado=6.4.1=py310ha75aee5_1\n  - traitlets=5.14.3=pyhd8ed1ab_0\n  - typing-extensions=4.12.2=hd8ed1ab_0\n  - typing_extensions=4.12.2=pyha770c72_0\n  - tzdata=2024b=hc8b5060_0\n  - udunits2=2.2.28=h40f5838_3\n  - ukkonen=1.0.1=py310h3788b33_5\n  - unicodedata2=15.1.0=py310ha75aee5_1\n  - uriparser=0.9.8=hac33072_0\n  - urllib3=2.2.3=pyhd8ed1ab_0\n  - virtualenv=20.27.0=pyhd8ed1ab_0\n  - webob=1.8.8=pyhd8ed1ab_0\n  - wheel=0.44.0=pyhd8ed1ab_0\n  - wrapt=1.16.0=py310ha75aee5_1\n  - xerces-c=3.2.5=h988505b_2\n  - xorg-libx11=1.8.10=h4f16b4b_0\n  - xorg-libxau=1.0.11=hb9d3cd8_1\n  - xorg-libxdmcp=1.1.5=hb9d3cd8_0\n  - xorg-libxext=1.3.6=hb9d3cd8_0\n  - xorg-libxfixes=6.0.1=hb9d3cd8_0\n  - xorg-libxi=1.8.2=hb9d3cd8_0\n  - xorg-xextproto=7.3.0=hb9d3cd8_1004\n  - xorg-xorgproto=2024.1=hb9d3cd8_1\n  - xxhash=0.8.2=hd590300_0\n  - xz=5.2.6=h166bdaf_0\n  - yaml=0.2.5=h7f98852_2\n  - yarl=1.16.0=py310ha75aee5_0\n  - zarr=2.18.3=pyhd8ed1ab_0\n  - zict=3.0.0=pyhd8ed1ab_0\n  - zipp=3.20.2=pyhd8ed1ab_0\n  - zlib=1.3.1=hb9d3cd8_2\n  - zstandard=0.23.0=py310ha39cb0e_1\n  - zstd=1.5.6=ha6fb4c9_0\n  - pip:\n      - dask==2022.8.1\n      - numbagg==0.8.2\n      - numpy==1.23.0\n      - packaging==23.1\n      - pandas==1.5.3\n      - pytest==7.4.0\n      - python-dateutil==2.8.2\n      - pytz==2023.3\n      - scipy==1.11.1\n      - setuptools==68.0.0\nprefix: /opt/miniconda3/envs/testbed",
    "pydata__xarray-6744": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=conda_forge\n  - _openmp_mutex=4.5=2_gnu\n  - affine=2.4.0=pyhd8ed1ab_0\n  - aiobotocore=2.15.1=pyhd8ed1ab_0\n  - aiohappyeyeballs=2.4.3=pyhd8ed1ab_0\n  - aiohttp=3.10.10=py310h89163eb_0\n  - aioitertools=0.12.0=pyhd8ed1ab_0\n  - aiosignal=1.3.1=pyhd8ed1ab_0\n  - antlr-python-runtime=4.11.1=pyhd8ed1ab_0\n  - appdirs=1.4.4=pyh9f0ad1d_0\n  - asciitree=0.3.3=py_2\n  - async-timeout=4.0.3=pyhd8ed1ab_0\n  - attrs=24.2.0=pyh71513ae_0\n  - backports.zoneinfo=0.2.1=py310hff52083_9\n  - beautifulsoup4=4.12.3=pyha770c72_0\n  - blosc=1.21.6=hef167b5_0\n  - boto3=1.35.23=pyhd8ed1ab_0\n  - botocore=1.35.23=pyge310_1234567_0\n  - bottleneck=1.4.2=py310hf462985_0\n  - brotli=1.1.0=hb9d3cd8_2\n  - brotli-bin=1.1.0=hb9d3cd8_2\n  - brotli-python=1.1.0=py310hf71b8c6_2\n  - bzip2=1.0.8=h4bc722e_7\n  - c-ares=1.34.2=heb4867d_0\n  - ca-certificates=2024.8.30=hbcca054_0\n  - cached-property=1.5.2=hd8ed1ab_1\n  - cached_property=1.5.2=pyha770c72_1\n  - cartopy=0.24.0=py310h5eaa309_0\n  - cdat_info=8.2.1=pyhd8ed1ab_2\n  - cdms2=3.1.5=py310h366d46e_22\n  - cdtime=3.1.4=py310h7a088e3_13\n  - certifi=2024.8.30=pyhd8ed1ab_0\n  - cf-units=3.2.0=py310hf462985_6\n  - cffi=1.17.1=py310h8deb56e_0\n  - cfgrib=0.9.14.1=pyhd8ed1ab_0\n  - cfgv=3.3.1=pyhd8ed1ab_0\n  - cftime=1.6.4=py310hf462985_1\n  - charset-normalizer=3.4.0=pyhd8ed1ab_0\n  - click=8.1.7=unix_pyh707e725_0\n  - click-plugins=1.1.1=py_0\n  - cligj=0.7.2=pyhd8ed1ab_1\n  - cloudpickle=3.1.0=pyhd8ed1ab_1\n  - colorama=0.4.6=pyhd8ed1ab_0\n  - contourpy=1.3.0=py310h3788b33_2\n  - coverage=7.6.4=py310h89163eb_0\n  - curl=8.10.1=hbbe4b11_0\n  - cycler=0.12.1=pyhd8ed1ab_0\n  - cytoolz=1.0.0=py310ha75aee5_1\n  - distarray=2.12.2=pyh050c7b8_4\n  - distlib=0.3.9=pyhd8ed1ab_0\n  - distributed=2024.10.0=pyhd8ed1ab_0\n  - docopt-ng=0.9.0=pyhd8ed1ab_0\n  - eccodes=2.38.0=h8bb6dbc_0\n  - esmf=8.6.1=nompi_h4441c20_3\n  - esmpy=8.6.1=pyhc1e730c_0\n  - exceptiongroup=1.2.2=pyhd8ed1ab_0\n  - execnet=2.1.1=pyhd8ed1ab_0\n  - fasteners=0.17.3=pyhd8ed1ab_0\n  - filelock=3.16.1=pyhd8ed1ab_0\n  - findlibs=0.0.5=pyhd8ed1ab_0\n  - flexcache=0.3=pyhd8ed1ab_0\n  - flexparser=0.3.1=pyhd8ed1ab_0\n  - flox=0.9.12=pyhd8ed1ab_0\n  - fonttools=4.54.1=py310h89163eb_1\n  - freeglut=3.2.2=ha6d2627_3\n  - freetype=2.12.1=h267a509_2\n  - freexl=2.0.0=h743c826_0\n  - frozenlist=1.5.0=py310ha75aee5_0\n  - fsspec=2024.10.0=pyhff2d567_0\n  - future=1.0.0=pyhd8ed1ab_0\n  - g2clib=1.9.0=ha770c72_1\n  - geos=3.13.0=h5888daf_0\n  - geotiff=1.7.3=h77b800c_3\n  - giflib=5.2.2=hd590300_0\n  - h2=4.1.0=pyhd8ed1ab_0\n  - h5netcdf=1.4.0=pyhd8ed1ab_0\n  - h5py=3.12.1=nompi_py310h60e0fe6_102\n  - hdf4=4.2.15=h2a13503_7\n  - hdf5=1.14.3=nompi_hdf9ad27_105\n  - hpack=4.0.0=pyh9f0ad1d_0\n  - hyperframe=6.0.1=pyhd8ed1ab_0\n  - hypothesis=6.115.5=pyha770c72_0\n  - icu=75.1=he02047a_0\n  - identify=2.6.1=pyhd8ed1ab_0\n  - idna=3.10=pyhd8ed1ab_0\n  - importlib-metadata=8.5.0=pyha770c72_0\n  - importlib-resources=6.4.5=pyhd8ed1ab_0\n  - importlib_metadata=8.5.0=hd8ed1ab_0\n  - importlib_resources=6.4.5=pyhd8ed1ab_0\n  - iniconfig=2.0.0=pyhd8ed1ab_0\n  - iris=3.10.0=pyha770c72_1\n  - jasper=4.2.4=h536e39c_0\n  - jinja2=3.1.4=pyhd8ed1ab_0\n  - jmespath=1.0.1=pyhd8ed1ab_0\n  - json-c=0.18=h6688a6e_0\n  - jsonschema=4.23.0=pyhd8ed1ab_0\n  - jsonschema-specifications=2024.10.1=pyhd8ed1ab_0\n  - jupyter_core=5.7.2=pyh31011fe_1\n  - keyutils=1.6.1=h166bdaf_0\n  - kiwisolver=1.4.7=py310h3788b33_0\n  - krb5=1.21.3=h659f571_0\n  - lazy-object-proxy=1.10.0=py310h2372a71_0\n  - lcms2=2.16=hb7c19ff_0\n  - ld_impl_linux-64=2.43=h712a8e2_2\n  - lerc=4.0.0=h27087fc_0\n  - libaec=1.1.3=h59595ed_0\n  - libarchive=3.7.4=hfca40fe_0\n  - libblas=3.9.0=25_linux64_openblas\n  - libbrotlicommon=1.1.0=hb9d3cd8_2\n  - libbrotlidec=1.1.0=hb9d3cd8_2\n  - libbrotlienc=1.1.0=hb9d3cd8_2\n  - libcblas=3.9.0=25_linux64_openblas\n  - libcdms=3.1.2=h0cec689_129\n  - libcf=1.0.3=py310h1588dd5_117\n  - libcurl=8.10.1=hbbe4b11_0\n  - libdeflate=1.22=hb9d3cd8_0\n  - libedit=3.1.20191231=he28a2e2_2\n  - libev=4.33=hd590300_2\n  - libexpat=2.6.3=h5888daf_0\n  - libffi=3.4.2=h7f98852_5\n  - libgcc=14.2.0=h77fa898_1\n  - libgcc-ng=14.2.0=h69a702a_1\n  - libgdal-core=3.9.2=hd5b9bfb_7\n  - libgfortran=14.2.0=h69a702a_1\n  - libgfortran-ng=14.2.0=h69a702a_1\n  - libgfortran5=14.2.0=hd5240d6_1\n  - libglu=9.0.0=ha6d2627_1004\n  - libgomp=14.2.0=h77fa898_1\n  - libiconv=1.17=hd590300_2\n  - libjpeg-turbo=3.0.0=hd590300_1\n  - libkml=1.3.0=hf539b9f_1021\n  - liblapack=3.9.0=25_linux64_openblas\n  - libllvm14=14.0.6=hcd5def8_4\n  - libnetcdf=4.9.2=nompi_h135f659_114\n  - libnghttp2=1.64.0=h161d5f1_0\n  - libnsl=2.0.1=hd590300_0\n  - libopenblas=0.3.28=pthreads_h94d23a6_0\n  - libpng=1.6.44=hadc24fc_0\n  - librttopo=1.1.0=h97f6797_17\n  - libspatialite=5.1.0=h1b4f908_11\n  - libsqlite=3.47.0=hadc24fc_0\n  - libssh2=1.11.0=h0841786_0\n  - libstdcxx=14.2.0=hc0a3c3a_1\n  - libstdcxx-ng=14.2.0=h4852527_1\n  - libtiff=4.7.0=he137b08_1\n  - libudunits2=2.2.28=h40f5838_3\n  - libuuid=2.38.1=h0b41bf4_0\n  - libwebp-base=1.4.0=hd590300_0\n  - libxcb=1.17.0=h8a09558_0\n  - libxcrypt=4.4.36=hd590300_1\n  - libxml2=2.12.7=he7c6b58_4\n  - libxslt=1.1.39=h76b75d6_0\n  - libzip=1.11.1=hf83b1b0_0\n  - libzlib=1.3.1=hb9d3cd8_2\n  - llvmlite=0.43.0=py310h1a6248f_1\n  - locket=1.0.0=pyhd8ed1ab_0\n  - lxml=5.3.0=py310h6ee67d5_1\n  - lz4-c=1.9.4=hcb278e6_0\n  - lzo=2.10=hd590300_1001\n  - markupsafe=3.0.2=py310h89163eb_0\n  - matplotlib-base=3.9.2=py310h68603db_1\n  - minizip=4.0.7=h401b404_0\n  - msgpack-python=1.1.0=py310h3788b33_0\n  - multidict=6.1.0=py310h89163eb_1\n  - munkres=1.1.4=pyh9f0ad1d_0\n  - nbformat=5.10.4=pyhd8ed1ab_0\n  - nc-time-axis=1.4.1=pyhd8ed1ab_0\n  - nceplibs-g2c=1.9.0=ha39ef1c_1\n  - ncurses=6.5=he02047a_1\n  - netcdf-fortran=4.6.1=nompi_h22f9119_106\n  - netcdf4=1.7.1=nompi_py310h9f0ad05_102\n  - nodeenv=1.9.1=pyhd8ed1ab_0\n  - nomkl=1.0=h5ca1d4c_0\n  - numba=0.60.0=py310h5dc88bb_0\n  - numcodecs=0.13.1=py310h5eaa309_0\n  - numexpr=2.10.1=py310hdb6e06b_103\n  - numpy_groupies=0.11.2=pyhd8ed1ab_0\n  - openblas=0.3.28=pthreads_hbcdf1e8_0\n  - openjpeg=2.5.2=h488ebb8_0\n  - openssl=3.3.2=hb9d3cd8_0\n  - partd=1.4.2=pyhd8ed1ab_0\n  - patsy=0.5.6=pyhd8ed1ab_0\n  - pcre2=10.44=hba22ea6_2\n  - pillow=11.0.0=py310hfeaa1f3_0\n  - pint=0.24.3=pyhd8ed1ab_0\n  - pip=24.2=pyh8b19718_1\n  - pkgutil-resolve-name=1.3.10=pyhd8ed1ab_1\n  - platformdirs=4.3.6=pyhd8ed1ab_0\n  - pluggy=1.5.0=pyhd8ed1ab_0\n  - pooch=1.8.2=pyhd8ed1ab_0\n  - pre-commit=4.0.1=pyha770c72_0\n  - proj=9.5.0=h12925eb_0\n  - propcache=0.2.0=py310ha75aee5_2\n  - pseudonetcdf=3.4.0=pyhd8ed1ab_0\n  - psutil=6.0.0=py310ha75aee5_2\n  - pthread-stubs=0.4=hb9d3cd8_1002\n  - pycparser=2.22=pyhd8ed1ab_0\n  - pydap=3.5=pyhd8ed1ab_0\n  - pyparsing=3.2.0=pyhd8ed1ab_1\n  - pyproj=3.7.0=py310h2e9f774_0\n  - pyshp=2.3.1=pyhd8ed1ab_0\n  - pysocks=1.7.1=pyha2e5f31_6\n  - pytest-cov=5.0.0=pyhd8ed1ab_0\n  - pytest-env=1.1.5=pyhd8ed1ab_0\n  - pytest-xdist=3.6.1=pyhd8ed1ab_0\n  - python=3.10.15=h4a871b0_2_cpython\n  - python-eccodes=2.37.0=py310hf462985_0\n  - python-fastjsonschema=2.20.0=pyhd8ed1ab_0\n  - python-tzdata=2024.2=pyhd8ed1ab_0\n  - python-xxhash=3.5.0=py310ha75aee5_1\n  - python_abi=3.10=5_cp310\n  - pyyaml=6.0.2=py310ha75aee5_1\n  - qhull=2020.2=h434a139_5\n  - rasterio=1.4.1=py310hf6c6cbe_0\n  - readline=8.2=h8228510_1\n  - referencing=0.35.1=pyhd8ed1ab_0\n  - requests=2.32.3=pyhd8ed1ab_0\n  - rpds-py=0.20.0=py310h505e2c1_1\n  - s3transfer=0.10.3=pyhd8ed1ab_0\n  - seaborn=0.13.2=hd8ed1ab_2\n  - seaborn-base=0.13.2=pyhd8ed1ab_2\n  - shapely=2.0.6=py310had3dfd6_2\n  - six=1.16.0=pyh6c4a22f_0\n  - snappy=1.2.1=ha2e4443_0\n  - snuggs=1.4.7=pyhd8ed1ab_1\n  - sortedcontainers=2.4.0=pyhd8ed1ab_0\n  - soupsieve=2.5=pyhd8ed1ab_1\n  - sparse=0.15.4=pyh267e887_1\n  - sqlite=3.47.0=h9eae976_0\n  - statsmodels=0.14.4=py310hf462985_0\n  - tblib=3.0.0=pyhd8ed1ab_0\n  - tk=8.6.13=noxft_h4845f30_101\n  - toml=0.10.2=pyhd8ed1ab_0\n  - tomli=2.0.2=pyhd8ed1ab_0\n  - toolz=1.0.0=pyhd8ed1ab_0\n  - tornado=6.4.1=py310ha75aee5_1\n  - traitlets=5.14.3=pyhd8ed1ab_0\n  - typing-extensions=4.12.2=hd8ed1ab_0\n  - typing_extensions=4.12.2=pyha770c72_0\n  - tzdata=2024b=hc8b5060_0\n  - udunits2=2.2.28=h40f5838_3\n  - ukkonen=1.0.1=py310h3788b33_5\n  - unicodedata2=15.1.0=py310ha75aee5_1\n  - uriparser=0.9.8=hac33072_0\n  - urllib3=2.2.3=pyhd8ed1ab_0\n  - virtualenv=20.27.0=pyhd8ed1ab_0\n  - webob=1.8.8=pyhd8ed1ab_0\n  - wheel=0.44.0=pyhd8ed1ab_0\n  - wrapt=1.16.0=py310ha75aee5_1\n  - xerces-c=3.2.5=h988505b_2\n  - xorg-libx11=1.8.10=h4f16b4b_0\n  - xorg-libxau=1.0.11=hb9d3cd8_1\n  - xorg-libxdmcp=1.1.5=hb9d3cd8_0\n  - xorg-libxext=1.3.6=hb9d3cd8_0\n  - xorg-libxfixes=6.0.1=hb9d3cd8_0\n  - xorg-libxi=1.8.2=hb9d3cd8_0\n  - xorg-xextproto=7.3.0=hb9d3cd8_1004\n  - xorg-xorgproto=2024.1=hb9d3cd8_1\n  - xxhash=0.8.2=hd590300_0\n  - xz=5.2.6=h166bdaf_0\n  - yaml=0.2.5=h7f98852_2\n  - yarl=1.16.0=py310ha75aee5_0\n  - zarr=2.18.3=pyhd8ed1ab_0\n  - zict=3.0.0=pyhd8ed1ab_0\n  - zipp=3.20.2=pyhd8ed1ab_0\n  - zlib=1.3.1=hb9d3cd8_2\n  - zstandard=0.23.0=py310ha39cb0e_1\n  - zstd=1.5.6=ha6fb4c9_0\n  - pip:\n      - dask==2022.8.1\n      - numbagg==0.8.2\n      - numpy==1.23.0\n      - packaging==23.1\n      - pandas==1.5.3\n      - pytest==7.4.0\n      - python-dateutil==2.8.2\n      - pytz==2023.3\n      - scipy==1.11.1\n      - setuptools==68.0.0\nprefix: /opt/miniconda3/envs/testbed",
    "pydata__xarray-6938": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=conda_forge\n  - _openmp_mutex=4.5=2_gnu\n  - affine=2.4.0=pyhd8ed1ab_0\n  - aiobotocore=2.15.1=pyhd8ed1ab_0\n  - aiohappyeyeballs=2.4.3=pyhd8ed1ab_0\n  - aiohttp=3.10.10=py310h89163eb_0\n  - aioitertools=0.12.0=pyhd8ed1ab_0\n  - aiosignal=1.3.1=pyhd8ed1ab_0\n  - antlr-python-runtime=4.11.1=pyhd8ed1ab_0\n  - appdirs=1.4.4=pyh9f0ad1d_0\n  - asciitree=0.3.3=py_2\n  - async-timeout=4.0.3=pyhd8ed1ab_0\n  - attrs=24.2.0=pyh71513ae_0\n  - backports.zoneinfo=0.2.1=py310hff52083_9\n  - beautifulsoup4=4.12.3=pyha770c72_0\n  - blosc=1.21.6=hef167b5_0\n  - boto3=1.35.23=pyhd8ed1ab_0\n  - botocore=1.35.23=pyge310_1234567_0\n  - bottleneck=1.4.2=py310hf462985_0\n  - brotli=1.1.0=hb9d3cd8_2\n  - brotli-bin=1.1.0=hb9d3cd8_2\n  - brotli-python=1.1.0=py310hf71b8c6_2\n  - bzip2=1.0.8=h4bc722e_7\n  - c-ares=1.34.2=heb4867d_0\n  - ca-certificates=2024.8.30=hbcca054_0\n  - cached-property=1.5.2=hd8ed1ab_1\n  - cached_property=1.5.2=pyha770c72_1\n  - cartopy=0.24.0=py310h5eaa309_0\n  - cdat_info=8.2.1=pyhd8ed1ab_2\n  - cdms2=3.1.5=py310h366d46e_22\n  - cdtime=3.1.4=py310h7a088e3_13\n  - certifi=2024.8.30=pyhd8ed1ab_0\n  - cf-units=3.2.0=py310hf462985_6\n  - cffi=1.17.1=py310h8deb56e_0\n  - cfgrib=0.9.14.1=pyhd8ed1ab_0\n  - cfgv=3.3.1=pyhd8ed1ab_0\n  - cftime=1.6.4=py310hf462985_1\n  - charset-normalizer=3.4.0=pyhd8ed1ab_0\n  - click=8.1.7=unix_pyh707e725_0\n  - click-plugins=1.1.1=py_0\n  - cligj=0.7.2=pyhd8ed1ab_1\n  - cloudpickle=3.1.0=pyhd8ed1ab_1\n  - colorama=0.4.6=pyhd8ed1ab_0\n  - contourpy=1.3.0=py310h3788b33_2\n  - coverage=7.6.4=py310h89163eb_0\n  - curl=8.10.1=hbbe4b11_0\n  - cycler=0.12.1=pyhd8ed1ab_0\n  - cytoolz=1.0.0=py310ha75aee5_1\n  - distarray=2.12.2=pyh050c7b8_4\n  - distlib=0.3.9=pyhd8ed1ab_0\n  - distributed=2024.10.0=pyhd8ed1ab_0\n  - docopt-ng=0.9.0=pyhd8ed1ab_0\n  - eccodes=2.38.0=h8bb6dbc_0\n  - esmf=8.6.1=nompi_h4441c20_3\n  - esmpy=8.6.1=pyhc1e730c_0\n  - exceptiongroup=1.2.2=pyhd8ed1ab_0\n  - execnet=2.1.1=pyhd8ed1ab_0\n  - fasteners=0.17.3=pyhd8ed1ab_0\n  - filelock=3.16.1=pyhd8ed1ab_0\n  - findlibs=0.0.5=pyhd8ed1ab_0\n  - flexcache=0.3=pyhd8ed1ab_0\n  - flexparser=0.3.1=pyhd8ed1ab_0\n  - flox=0.9.12=pyhd8ed1ab_0\n  - fonttools=4.54.1=py310h89163eb_1\n  - freeglut=3.2.2=ha6d2627_3\n  - freetype=2.12.1=h267a509_2\n  - freexl=2.0.0=h743c826_0\n  - frozenlist=1.5.0=py310ha75aee5_0\n  - fsspec=2024.10.0=pyhff2d567_0\n  - future=1.0.0=pyhd8ed1ab_0\n  - g2clib=1.9.0=ha770c72_1\n  - geos=3.13.0=h5888daf_0\n  - geotiff=1.7.3=h77b800c_3\n  - giflib=5.2.2=hd590300_0\n  - h2=4.1.0=pyhd8ed1ab_0\n  - h5netcdf=1.4.0=pyhd8ed1ab_0\n  - h5py=3.12.1=nompi_py310h60e0fe6_102\n  - hdf4=4.2.15=h2a13503_7\n  - hdf5=1.14.3=nompi_hdf9ad27_105\n  - hpack=4.0.0=pyh9f0ad1d_0\n  - hyperframe=6.0.1=pyhd8ed1ab_0\n  - hypothesis=6.115.5=pyha770c72_0\n  - icu=75.1=he02047a_0\n  - identify=2.6.1=pyhd8ed1ab_0\n  - idna=3.10=pyhd8ed1ab_0\n  - importlib-metadata=8.5.0=pyha770c72_0\n  - importlib-resources=6.4.5=pyhd8ed1ab_0\n  - importlib_metadata=8.5.0=hd8ed1ab_0\n  - importlib_resources=6.4.5=pyhd8ed1ab_0\n  - iniconfig=2.0.0=pyhd8ed1ab_0\n  - iris=3.10.0=pyha770c72_1\n  - jasper=4.2.4=h536e39c_0\n  - jinja2=3.1.4=pyhd8ed1ab_0\n  - jmespath=1.0.1=pyhd8ed1ab_0\n  - json-c=0.18=h6688a6e_0\n  - jsonschema=4.23.0=pyhd8ed1ab_0\n  - jsonschema-specifications=2024.10.1=pyhd8ed1ab_0\n  - jupyter_core=5.7.2=pyh31011fe_1\n  - keyutils=1.6.1=h166bdaf_0\n  - kiwisolver=1.4.7=py310h3788b33_0\n  - krb5=1.21.3=h659f571_0\n  - lazy-object-proxy=1.10.0=py310h2372a71_0\n  - lcms2=2.16=hb7c19ff_0\n  - ld_impl_linux-64=2.43=h712a8e2_2\n  - lerc=4.0.0=h27087fc_0\n  - libaec=1.1.3=h59595ed_0\n  - libarchive=3.7.4=hfca40fe_0\n  - libblas=3.9.0=25_linux64_openblas\n  - libbrotlicommon=1.1.0=hb9d3cd8_2\n  - libbrotlidec=1.1.0=hb9d3cd8_2\n  - libbrotlienc=1.1.0=hb9d3cd8_2\n  - libcblas=3.9.0=25_linux64_openblas\n  - libcdms=3.1.2=h0cec689_129\n  - libcf=1.0.3=py310h1588dd5_117\n  - libcurl=8.10.1=hbbe4b11_0\n  - libdeflate=1.22=hb9d3cd8_0\n  - libedit=3.1.20191231=he28a2e2_2\n  - libev=4.33=hd590300_2\n  - libexpat=2.6.3=h5888daf_0\n  - libffi=3.4.2=h7f98852_5\n  - libgcc=14.2.0=h77fa898_1\n  - libgcc-ng=14.2.0=h69a702a_1\n  - libgdal-core=3.9.2=hd5b9bfb_7\n  - libgfortran=14.2.0=h69a702a_1\n  - libgfortran-ng=14.2.0=h69a702a_1\n  - libgfortran5=14.2.0=hd5240d6_1\n  - libglu=9.0.0=ha6d2627_1004\n  - libgomp=14.2.0=h77fa898_1\n  - libiconv=1.17=hd590300_2\n  - libjpeg-turbo=3.0.0=hd590300_1\n  - libkml=1.3.0=hf539b9f_1021\n  - liblapack=3.9.0=25_linux64_openblas\n  - libllvm14=14.0.6=hcd5def8_4\n  - libnetcdf=4.9.2=nompi_h135f659_114\n  - libnghttp2=1.64.0=h161d5f1_0\n  - libnsl=2.0.1=hd590300_0\n  - libopenblas=0.3.28=pthreads_h94d23a6_0\n  - libpng=1.6.44=hadc24fc_0\n  - librttopo=1.1.0=h97f6797_17\n  - libspatialite=5.1.0=h1b4f908_11\n  - libsqlite=3.47.0=hadc24fc_0\n  - libssh2=1.11.0=h0841786_0\n  - libstdcxx=14.2.0=hc0a3c3a_1\n  - libstdcxx-ng=14.2.0=h4852527_1\n  - libtiff=4.7.0=he137b08_1\n  - libudunits2=2.2.28=h40f5838_3\n  - libuuid=2.38.1=h0b41bf4_0\n  - libwebp-base=1.4.0=hd590300_0\n  - libxcb=1.17.0=h8a09558_0\n  - libxcrypt=4.4.36=hd590300_1\n  - libxml2=2.12.7=he7c6b58_4\n  - libxslt=1.1.39=h76b75d6_0\n  - libzip=1.11.1=hf83b1b0_0\n  - libzlib=1.3.1=hb9d3cd8_2\n  - llvmlite=0.43.0=py310h1a6248f_1\n  - locket=1.0.0=pyhd8ed1ab_0\n  - lxml=5.3.0=py310h6ee67d5_1\n  - lz4-c=1.9.4=hcb278e6_0\n  - lzo=2.10=hd590300_1001\n  - markupsafe=3.0.2=py310h89163eb_0\n  - matplotlib-base=3.9.2=py310h68603db_1\n  - minizip=4.0.7=h401b404_0\n  - msgpack-python=1.1.0=py310h3788b33_0\n  - multidict=6.1.0=py310h89163eb_1\n  - munkres=1.1.4=pyh9f0ad1d_0\n  - nbformat=5.10.4=pyhd8ed1ab_0\n  - nc-time-axis=1.4.1=pyhd8ed1ab_0\n  - nceplibs-g2c=1.9.0=ha39ef1c_1\n  - ncurses=6.5=he02047a_1\n  - netcdf-fortran=4.6.1=nompi_h22f9119_106\n  - netcdf4=1.7.1=nompi_py310h9f0ad05_102\n  - nodeenv=1.9.1=pyhd8ed1ab_0\n  - nomkl=1.0=h5ca1d4c_0\n  - numba=0.60.0=py310h5dc88bb_0\n  - numcodecs=0.13.1=py310h5eaa309_0\n  - numexpr=2.10.1=py310hdb6e06b_103\n  - numpy_groupies=0.11.2=pyhd8ed1ab_0\n  - openblas=0.3.28=pthreads_hbcdf1e8_0\n  - openjpeg=2.5.2=h488ebb8_0\n  - openssl=3.3.2=hb9d3cd8_0\n  - partd=1.4.2=pyhd8ed1ab_0\n  - patsy=0.5.6=pyhd8ed1ab_0\n  - pcre2=10.44=hba22ea6_2\n  - pillow=11.0.0=py310hfeaa1f3_0\n  - pint=0.24.3=pyhd8ed1ab_0\n  - pip=24.2=pyh8b19718_1\n  - pkgutil-resolve-name=1.3.10=pyhd8ed1ab_1\n  - platformdirs=4.3.6=pyhd8ed1ab_0\n  - pluggy=1.5.0=pyhd8ed1ab_0\n  - pooch=1.8.2=pyhd8ed1ab_0\n  - pre-commit=4.0.1=pyha770c72_0\n  - proj=9.5.0=h12925eb_0\n  - propcache=0.2.0=py310ha75aee5_2\n  - pseudonetcdf=3.4.0=pyhd8ed1ab_0\n  - psutil=6.0.0=py310ha75aee5_2\n  - pthread-stubs=0.4=hb9d3cd8_1002\n  - pycparser=2.22=pyhd8ed1ab_0\n  - pydap=3.5=pyhd8ed1ab_0\n  - pyparsing=3.2.0=pyhd8ed1ab_1\n  - pyproj=3.7.0=py310h2e9f774_0\n  - pyshp=2.3.1=pyhd8ed1ab_0\n  - pysocks=1.7.1=pyha2e5f31_6\n  - pytest-cov=5.0.0=pyhd8ed1ab_0\n  - pytest-env=1.1.5=pyhd8ed1ab_0\n  - pytest-xdist=3.6.1=pyhd8ed1ab_0\n  - python=3.10.15=h4a871b0_2_cpython\n  - python-eccodes=2.37.0=py310hf462985_0\n  - python-fastjsonschema=2.20.0=pyhd8ed1ab_0\n  - python-tzdata=2024.2=pyhd8ed1ab_0\n  - python-xxhash=3.5.0=py310ha75aee5_1\n  - python_abi=3.10=5_cp310\n  - pyyaml=6.0.2=py310ha75aee5_1\n  - qhull=2020.2=h434a139_5\n  - rasterio=1.4.1=py310hf6c6cbe_0\n  - readline=8.2=h8228510_1\n  - referencing=0.35.1=pyhd8ed1ab_0\n  - requests=2.32.3=pyhd8ed1ab_0\n  - rpds-py=0.20.0=py310h505e2c1_1\n  - s3transfer=0.10.3=pyhd8ed1ab_0\n  - seaborn=0.13.2=hd8ed1ab_2\n  - seaborn-base=0.13.2=pyhd8ed1ab_2\n  - shapely=2.0.6=py310had3dfd6_2\n  - six=1.16.0=pyh6c4a22f_0\n  - snappy=1.2.1=ha2e4443_0\n  - snuggs=1.4.7=pyhd8ed1ab_1\n  - sortedcontainers=2.4.0=pyhd8ed1ab_0\n  - soupsieve=2.5=pyhd8ed1ab_1\n  - sparse=0.15.4=pyh267e887_1\n  - sqlite=3.47.0=h9eae976_0\n  - statsmodels=0.14.4=py310hf462985_0\n  - tblib=3.0.0=pyhd8ed1ab_0\n  - tk=8.6.13=noxft_h4845f30_101\n  - toml=0.10.2=pyhd8ed1ab_0\n  - tomli=2.0.2=pyhd8ed1ab_0\n  - toolz=1.0.0=pyhd8ed1ab_0\n  - tornado=6.4.1=py310ha75aee5_1\n  - traitlets=5.14.3=pyhd8ed1ab_0\n  - typing-extensions=4.12.2=hd8ed1ab_0\n  - typing_extensions=4.12.2=pyha770c72_0\n  - tzdata=2024b=hc8b5060_0\n  - udunits2=2.2.28=h40f5838_3\n  - ukkonen=1.0.1=py310h3788b33_5\n  - unicodedata2=15.1.0=py310ha75aee5_1\n  - uriparser=0.9.8=hac33072_0\n  - urllib3=2.2.3=pyhd8ed1ab_0\n  - virtualenv=20.27.0=pyhd8ed1ab_0\n  - webob=1.8.8=pyhd8ed1ab_0\n  - wheel=0.44.0=pyhd8ed1ab_0\n  - wrapt=1.16.0=py310ha75aee5_1\n  - xerces-c=3.2.5=h988505b_2\n  - xorg-libx11=1.8.10=h4f16b4b_0\n  - xorg-libxau=1.0.11=hb9d3cd8_1\n  - xorg-libxdmcp=1.1.5=hb9d3cd8_0\n  - xorg-libxext=1.3.6=hb9d3cd8_0\n  - xorg-libxfixes=6.0.1=hb9d3cd8_0\n  - xorg-libxi=1.8.2=hb9d3cd8_0\n  - xorg-xextproto=7.3.0=hb9d3cd8_1004\n  - xorg-xorgproto=2024.1=hb9d3cd8_1\n  - xxhash=0.8.2=hd590300_0\n  - xz=5.2.6=h166bdaf_0\n  - yaml=0.2.5=h7f98852_2\n  - yarl=1.16.0=py310ha75aee5_0\n  - zarr=2.18.3=pyhd8ed1ab_0\n  - zict=3.0.0=pyhd8ed1ab_0\n  - zipp=3.20.2=pyhd8ed1ab_0\n  - zlib=1.3.1=hb9d3cd8_2\n  - zstandard=0.23.0=py310ha39cb0e_1\n  - zstd=1.5.6=ha6fb4c9_0\n  - pip:\n      - dask==2022.8.1\n      - numbagg==0.8.2\n      - numpy==1.23.0\n      - packaging==23.1\n      - pandas==1.5.3\n      - pytest==7.4.0\n      - python-dateutil==2.8.2\n      - pytz==2023.3\n      - scipy==1.11.1\n      - setuptools==68.0.0\nprefix: /opt/miniconda3/envs/testbed",
    "pydata__xarray-6992": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=conda_forge\n  - _openmp_mutex=4.5=2_gnu\n  - affine=2.4.0=pyhd8ed1ab_0\n  - aiobotocore=2.15.1=pyhd8ed1ab_0\n  - aiohappyeyeballs=2.4.3=pyhd8ed1ab_0\n  - aiohttp=3.10.10=py310h89163eb_0\n  - aioitertools=0.12.0=pyhd8ed1ab_0\n  - aiosignal=1.3.1=pyhd8ed1ab_0\n  - antlr-python-runtime=4.11.1=pyhd8ed1ab_0\n  - appdirs=1.4.4=pyh9f0ad1d_0\n  - asciitree=0.3.3=py_2\n  - async-timeout=4.0.3=pyhd8ed1ab_0\n  - attrs=24.2.0=pyh71513ae_0\n  - backports.zoneinfo=0.2.1=py310hff52083_9\n  - beautifulsoup4=4.12.3=pyha770c72_0\n  - blosc=1.21.6=hef167b5_0\n  - boto3=1.35.23=pyhd8ed1ab_0\n  - botocore=1.35.23=pyge310_1234567_0\n  - bottleneck=1.4.2=py310hf462985_0\n  - brotli=1.1.0=hb9d3cd8_2\n  - brotli-bin=1.1.0=hb9d3cd8_2\n  - brotli-python=1.1.0=py310hf71b8c6_2\n  - bzip2=1.0.8=h4bc722e_7\n  - c-ares=1.34.2=heb4867d_0\n  - ca-certificates=2024.8.30=hbcca054_0\n  - cached-property=1.5.2=hd8ed1ab_1\n  - cached_property=1.5.2=pyha770c72_1\n  - cartopy=0.24.0=py310h5eaa309_0\n  - cdat_info=8.2.1=pyhd8ed1ab_2\n  - cdms2=3.1.5=py310h366d46e_22\n  - cdtime=3.1.4=py310h7a088e3_13\n  - certifi=2024.8.30=pyhd8ed1ab_0\n  - cf-units=3.2.0=py310hf462985_6\n  - cffi=1.17.1=py310h8deb56e_0\n  - cfgrib=0.9.14.1=pyhd8ed1ab_0\n  - cfgv=3.3.1=pyhd8ed1ab_0\n  - cftime=1.6.4=py310hf462985_1\n  - charset-normalizer=3.4.0=pyhd8ed1ab_0\n  - click=8.1.7=unix_pyh707e725_0\n  - click-plugins=1.1.1=py_0\n  - cligj=0.7.2=pyhd8ed1ab_1\n  - cloudpickle=3.1.0=pyhd8ed1ab_1\n  - colorama=0.4.6=pyhd8ed1ab_0\n  - contourpy=1.3.0=py310h3788b33_2\n  - coverage=7.6.4=py310h89163eb_0\n  - curl=8.10.1=hbbe4b11_0\n  - cycler=0.12.1=pyhd8ed1ab_0\n  - cytoolz=1.0.0=py310ha75aee5_1\n  - distarray=2.12.2=pyh050c7b8_4\n  - distlib=0.3.9=pyhd8ed1ab_0\n  - distributed=2024.10.0=pyhd8ed1ab_0\n  - docopt-ng=0.9.0=pyhd8ed1ab_0\n  - eccodes=2.38.0=h8bb6dbc_0\n  - esmf=8.6.1=nompi_h4441c20_3\n  - esmpy=8.6.1=pyhc1e730c_0\n  - exceptiongroup=1.2.2=pyhd8ed1ab_0\n  - execnet=2.1.1=pyhd8ed1ab_0\n  - fasteners=0.17.3=pyhd8ed1ab_0\n  - filelock=3.16.1=pyhd8ed1ab_0\n  - findlibs=0.0.5=pyhd8ed1ab_0\n  - flexcache=0.3=pyhd8ed1ab_0\n  - flexparser=0.3.1=pyhd8ed1ab_0\n  - flox=0.9.12=pyhd8ed1ab_0\n  - fonttools=4.54.1=py310h89163eb_1\n  - freeglut=3.2.2=ha6d2627_3\n  - freetype=2.12.1=h267a509_2\n  - freexl=2.0.0=h743c826_0\n  - frozenlist=1.5.0=py310ha75aee5_0\n  - fsspec=2024.10.0=pyhff2d567_0\n  - future=1.0.0=pyhd8ed1ab_0\n  - g2clib=1.9.0=ha770c72_1\n  - geos=3.13.0=h5888daf_0\n  - geotiff=1.7.3=h77b800c_3\n  - giflib=5.2.2=hd590300_0\n  - h2=4.1.0=pyhd8ed1ab_0\n  - h5netcdf=1.4.0=pyhd8ed1ab_0\n  - h5py=3.12.1=nompi_py310h60e0fe6_102\n  - hdf4=4.2.15=h2a13503_7\n  - hdf5=1.14.3=nompi_hdf9ad27_105\n  - hpack=4.0.0=pyh9f0ad1d_0\n  - hyperframe=6.0.1=pyhd8ed1ab_0\n  - hypothesis=6.115.5=pyha770c72_0\n  - icu=75.1=he02047a_0\n  - identify=2.6.1=pyhd8ed1ab_0\n  - idna=3.10=pyhd8ed1ab_0\n  - importlib-metadata=8.5.0=pyha770c72_0\n  - importlib-resources=6.4.5=pyhd8ed1ab_0\n  - importlib_metadata=8.5.0=hd8ed1ab_0\n  - importlib_resources=6.4.5=pyhd8ed1ab_0\n  - iniconfig=2.0.0=pyhd8ed1ab_0\n  - iris=3.10.0=pyha770c72_1\n  - jasper=4.2.4=h536e39c_0\n  - jinja2=3.1.4=pyhd8ed1ab_0\n  - jmespath=1.0.1=pyhd8ed1ab_0\n  - json-c=0.18=h6688a6e_0\n  - jsonschema=4.23.0=pyhd8ed1ab_0\n  - jsonschema-specifications=2024.10.1=pyhd8ed1ab_0\n  - jupyter_core=5.7.2=pyh31011fe_1\n  - keyutils=1.6.1=h166bdaf_0\n  - kiwisolver=1.4.7=py310h3788b33_0\n  - krb5=1.21.3=h659f571_0\n  - lazy-object-proxy=1.10.0=py310h2372a71_0\n  - lcms2=2.16=hb7c19ff_0\n  - ld_impl_linux-64=2.43=h712a8e2_2\n  - lerc=4.0.0=h27087fc_0\n  - libaec=1.1.3=h59595ed_0\n  - libarchive=3.7.4=hfca40fe_0\n  - libblas=3.9.0=25_linux64_openblas\n  - libbrotlicommon=1.1.0=hb9d3cd8_2\n  - libbrotlidec=1.1.0=hb9d3cd8_2\n  - libbrotlienc=1.1.0=hb9d3cd8_2\n  - libcblas=3.9.0=25_linux64_openblas\n  - libcdms=3.1.2=h0cec689_129\n  - libcf=1.0.3=py310h1588dd5_117\n  - libcurl=8.10.1=hbbe4b11_0\n  - libdeflate=1.22=hb9d3cd8_0\n  - libedit=3.1.20191231=he28a2e2_2\n  - libev=4.33=hd590300_2\n  - libexpat=2.6.3=h5888daf_0\n  - libffi=3.4.2=h7f98852_5\n  - libgcc=14.2.0=h77fa898_1\n  - libgcc-ng=14.2.0=h69a702a_1\n  - libgdal-core=3.9.2=hd5b9bfb_7\n  - libgfortran=14.2.0=h69a702a_1\n  - libgfortran-ng=14.2.0=h69a702a_1\n  - libgfortran5=14.2.0=hd5240d6_1\n  - libglu=9.0.0=ha6d2627_1004\n  - libgomp=14.2.0=h77fa898_1\n  - libiconv=1.17=hd590300_2\n  - libjpeg-turbo=3.0.0=hd590300_1\n  - libkml=1.3.0=hf539b9f_1021\n  - liblapack=3.9.0=25_linux64_openblas\n  - libllvm14=14.0.6=hcd5def8_4\n  - libnetcdf=4.9.2=nompi_h135f659_114\n  - libnghttp2=1.64.0=h161d5f1_0\n  - libnsl=2.0.1=hd590300_0\n  - libopenblas=0.3.28=pthreads_h94d23a6_0\n  - libpng=1.6.44=hadc24fc_0\n  - librttopo=1.1.0=h97f6797_17\n  - libspatialite=5.1.0=h1b4f908_11\n  - libsqlite=3.47.0=hadc24fc_0\n  - libssh2=1.11.0=h0841786_0\n  - libstdcxx=14.2.0=hc0a3c3a_1\n  - libstdcxx-ng=14.2.0=h4852527_1\n  - libtiff=4.7.0=he137b08_1\n  - libudunits2=2.2.28=h40f5838_3\n  - libuuid=2.38.1=h0b41bf4_0\n  - libwebp-base=1.4.0=hd590300_0\n  - libxcb=1.17.0=h8a09558_0\n  - libxcrypt=4.4.36=hd590300_1\n  - libxml2=2.12.7=he7c6b58_4\n  - libxslt=1.1.39=h76b75d6_0\n  - libzip=1.11.1=hf83b1b0_0\n  - libzlib=1.3.1=hb9d3cd8_2\n  - llvmlite=0.43.0=py310h1a6248f_1\n  - locket=1.0.0=pyhd8ed1ab_0\n  - lxml=5.3.0=py310h6ee67d5_1\n  - lz4-c=1.9.4=hcb278e6_0\n  - lzo=2.10=hd590300_1001\n  - markupsafe=3.0.2=py310h89163eb_0\n  - matplotlib-base=3.9.2=py310h68603db_1\n  - minizip=4.0.7=h401b404_0\n  - msgpack-python=1.1.0=py310h3788b33_0\n  - multidict=6.1.0=py310h89163eb_1\n  - munkres=1.1.4=pyh9f0ad1d_0\n  - nbformat=5.10.4=pyhd8ed1ab_0\n  - nc-time-axis=1.4.1=pyhd8ed1ab_0\n  - nceplibs-g2c=1.9.0=ha39ef1c_1\n  - ncurses=6.5=he02047a_1\n  - netcdf-fortran=4.6.1=nompi_h22f9119_106\n  - netcdf4=1.7.1=nompi_py310h9f0ad05_102\n  - nodeenv=1.9.1=pyhd8ed1ab_0\n  - nomkl=1.0=h5ca1d4c_0\n  - numba=0.60.0=py310h5dc88bb_0\n  - numcodecs=0.13.1=py310h5eaa309_0\n  - numexpr=2.10.1=py310hdb6e06b_103\n  - numpy_groupies=0.11.2=pyhd8ed1ab_0\n  - openblas=0.3.28=pthreads_hbcdf1e8_0\n  - openjpeg=2.5.2=h488ebb8_0\n  - openssl=3.3.2=hb9d3cd8_0\n  - partd=1.4.2=pyhd8ed1ab_0\n  - patsy=0.5.6=pyhd8ed1ab_0\n  - pcre2=10.44=hba22ea6_2\n  - pillow=11.0.0=py310hfeaa1f3_0\n  - pint=0.24.3=pyhd8ed1ab_0\n  - pip=24.2=pyh8b19718_1\n  - pkgutil-resolve-name=1.3.10=pyhd8ed1ab_1\n  - platformdirs=4.3.6=pyhd8ed1ab_0\n  - pluggy=1.5.0=pyhd8ed1ab_0\n  - pooch=1.8.2=pyhd8ed1ab_0\n  - pre-commit=4.0.1=pyha770c72_0\n  - proj=9.5.0=h12925eb_0\n  - propcache=0.2.0=py310ha75aee5_2\n  - pseudonetcdf=3.4.0=pyhd8ed1ab_0\n  - psutil=6.0.0=py310ha75aee5_2\n  - pthread-stubs=0.4=hb9d3cd8_1002\n  - pycparser=2.22=pyhd8ed1ab_0\n  - pydap=3.5=pyhd8ed1ab_0\n  - pyparsing=3.2.0=pyhd8ed1ab_1\n  - pyproj=3.7.0=py310h2e9f774_0\n  - pyshp=2.3.1=pyhd8ed1ab_0\n  - pysocks=1.7.1=pyha2e5f31_6\n  - pytest-cov=5.0.0=pyhd8ed1ab_0\n  - pytest-env=1.1.5=pyhd8ed1ab_0\n  - pytest-xdist=3.6.1=pyhd8ed1ab_0\n  - python=3.10.15=h4a871b0_2_cpython\n  - python-eccodes=2.37.0=py310hf462985_0\n  - python-fastjsonschema=2.20.0=pyhd8ed1ab_0\n  - python-tzdata=2024.2=pyhd8ed1ab_0\n  - python-xxhash=3.5.0=py310ha75aee5_1\n  - python_abi=3.10=5_cp310\n  - pyyaml=6.0.2=py310ha75aee5_1\n  - qhull=2020.2=h434a139_5\n  - rasterio=1.4.1=py310hf6c6cbe_0\n  - readline=8.2=h8228510_1\n  - referencing=0.35.1=pyhd8ed1ab_0\n  - requests=2.32.3=pyhd8ed1ab_0\n  - rpds-py=0.20.0=py310h505e2c1_1\n  - s3transfer=0.10.3=pyhd8ed1ab_0\n  - seaborn=0.13.2=hd8ed1ab_2\n  - seaborn-base=0.13.2=pyhd8ed1ab_2\n  - shapely=2.0.6=py310had3dfd6_2\n  - six=1.16.0=pyh6c4a22f_0\n  - snappy=1.2.1=ha2e4443_0\n  - snuggs=1.4.7=pyhd8ed1ab_1\n  - sortedcontainers=2.4.0=pyhd8ed1ab_0\n  - soupsieve=2.5=pyhd8ed1ab_1\n  - sparse=0.15.4=pyh267e887_1\n  - sqlite=3.47.0=h9eae976_0\n  - statsmodels=0.14.4=py310hf462985_0\n  - tblib=3.0.0=pyhd8ed1ab_0\n  - tk=8.6.13=noxft_h4845f30_101\n  - toml=0.10.2=pyhd8ed1ab_0\n  - tomli=2.0.2=pyhd8ed1ab_0\n  - toolz=1.0.0=pyhd8ed1ab_0\n  - tornado=6.4.1=py310ha75aee5_1\n  - traitlets=5.14.3=pyhd8ed1ab_0\n  - typing-extensions=4.12.2=hd8ed1ab_0\n  - typing_extensions=4.12.2=pyha770c72_0\n  - tzdata=2024b=hc8b5060_0\n  - udunits2=2.2.28=h40f5838_3\n  - ukkonen=1.0.1=py310h3788b33_5\n  - unicodedata2=15.1.0=py310ha75aee5_1\n  - uriparser=0.9.8=hac33072_0\n  - urllib3=2.2.3=pyhd8ed1ab_0\n  - virtualenv=20.27.0=pyhd8ed1ab_0\n  - webob=1.8.8=pyhd8ed1ab_0\n  - wheel=0.44.0=pyhd8ed1ab_0\n  - wrapt=1.16.0=py310ha75aee5_1\n  - xerces-c=3.2.5=h988505b_2\n  - xorg-libx11=1.8.10=h4f16b4b_0\n  - xorg-libxau=1.0.11=hb9d3cd8_1\n  - xorg-libxdmcp=1.1.5=hb9d3cd8_0\n  - xorg-libxext=1.3.6=hb9d3cd8_0\n  - xorg-libxfixes=6.0.1=hb9d3cd8_0\n  - xorg-libxi=1.8.2=hb9d3cd8_0\n  - xorg-xextproto=7.3.0=hb9d3cd8_1004\n  - xorg-xorgproto=2024.1=hb9d3cd8_1\n  - xxhash=0.8.2=hd590300_0\n  - xz=5.2.6=h166bdaf_0\n  - yaml=0.2.5=h7f98852_2\n  - yarl=1.16.0=py310ha75aee5_0\n  - zarr=2.18.3=pyhd8ed1ab_0\n  - zict=3.0.0=pyhd8ed1ab_0\n  - zipp=3.20.2=pyhd8ed1ab_0\n  - zlib=1.3.1=hb9d3cd8_2\n  - zstandard=0.23.0=py310ha39cb0e_1\n  - zstd=1.5.6=ha6fb4c9_0\n  - pip:\n      - dask==2022.8.1\n      - numbagg==0.8.2\n      - numpy==1.23.0\n      - packaging==23.1\n      - pandas==1.5.3\n      - pytest==7.4.0\n      - python-dateutil==2.8.2\n      - pytz==2023.3\n      - scipy==1.11.1\n      - setuptools==68.0.0\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-10051": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - attrs==23.1.0\n      - iniconfig==2.0.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - tomli==2.0.1\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-10081": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - attrs==23.1.0\n      - iniconfig==2.0.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - tomli==2.0.1\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-10356": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - attrs==23.1.0\n      - exceptiongroup==1.2.2\n      - iniconfig==2.0.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - tomli==2.0.1\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-5262": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - atomicwrites==1.4.1\n      - attrs==23.1.0\n      - more-itertools==10.1.0\n      - pluggy==0.11.0\n      - py==1.11.0\n      - setuptools==68.0.0\n      - six==1.16.0\n      - wcwidth==0.2.6\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-5631": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - atomicwrites==1.4.1\n      - attrs==23.1.0\n      - importlib-metadata==8.5.0\n      - more-itertools==10.1.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - wcwidth==0.2.6\n      - zipp==3.20.2\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-5787": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - atomicwrites==1.4.1\n      - attrs==23.1.0\n      - more-itertools==10.1.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - wcwidth==0.2.6\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-5809": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - atomicwrites==1.4.1\n      - attrs==23.1.0\n      - importlib-metadata==8.5.0\n      - more-itertools==10.1.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - six==1.16.0\n      - wcwidth==0.2.6\n      - zipp==3.20.2\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-5840": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - atomicwrites==1.4.1\n      - attrs==23.1.0\n      - more-itertools==10.1.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - wcwidth==0.2.6\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-6197": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - atomicwrites==1.4.1\n      - attrs==23.1.0\n      - more-itertools==10.1.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - wcwidth==0.2.6\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-6202": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - atomicwrites==1.4.1\n      - attrs==23.1.0\n      - more-itertools==10.1.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - wcwidth==0.2.6\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-7205": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - attrs==23.1.0\n      - more-itertools==10.1.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - wcwidth==0.2.13\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-7236": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - attrs==23.1.0\n      - more-itertools==10.1.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - wcwidth==0.2.13\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-7324": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - attrs==23.1.0\n      - iniconfig==2.0.0\n      - more-itertools==10.1.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-7432": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - attrs==23.1.0\n      - iniconfig==2.0.0\n      - more-itertools==10.1.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - toml==0.10.2\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-7490": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - attrs==23.1.0\n      - iniconfig==2.0.0\n      - more-itertools==10.1.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - toml==0.10.2\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-7521": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - attrs==23.1.0\n      - iniconfig==2.0.0\n      - more-itertools==10.1.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - toml==0.10.2\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-7571": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - attrs==23.1.0\n      - iniconfig==2.0.0\n      - more-itertools==10.1.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - toml==0.10.2\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-7982": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - attrs==23.1.0\n      - iniconfig==2.0.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - toml==0.10.2\nprefix: /opt/miniconda3/envs/testbed",
    "pytest-dev__pytest-8399": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - attrs==23.1.0\n      - iniconfig==2.0.0\n      - packaging==23.1\n      - pluggy==0.13.1\n      - py==1.11.0\n      - toml==0.10.2\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-10323": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.16\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.17.1\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - importlib-metadata==8.5.0\n      - iniconfig==2.0.0\n      - jinja2==3.1.4\n      - markupsafe==3.0.2\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\n      - zipp==3.20.2\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-10435": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.16\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.18.1\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - importlib-metadata==8.5.0\n      - iniconfig==2.0.0\n      - jinja2==3.1.4\n      - markupsafe==3.0.2\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\n      - zipp==3.20.2\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-7440": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - typed-ast==1.5.5\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-7454": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - typed-ast==1.5.5\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-7462": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - typed-ast==1.5.5\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-7590": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - typed-ast==1.5.5\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-7748": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - typed-ast==1.5.5\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-7757": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - typed-ast==1.5.5\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-7889": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - typed-ast==1.5.5\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-7910": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - typed-ast==1.5.5\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-7985": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - typed-ast==1.5.5\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-8035": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.11.26=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.21=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.12.14\n      - chardet==5.2.0\n      - charset-normalizer==3.4.1\n      - colorama==0.4.6\n      - coverage==7.6.10\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.2\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.4\n      - pytest-cov==6.0.0\n      - requests==2.32.3\n      - six==1.17.0\n      - snowballstemmer==2.2.0\n      - tomli==2.2.1\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - typed-ast==1.5.5\n      - urllib3==2.3.0\n      - virtualenv==20.28.1\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-8056": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - typed-ast==1.5.5\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-8120": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - typed-ast==1.5.5\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-8269": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - typed-ast==1.5.5\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-8459": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - typed-ast==1.5.5\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-8475": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.11.26=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.21=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.12.14\n      - chardet==5.2.0\n      - charset-normalizer==3.4.1\n      - colorama==0.4.6\n      - coverage==7.6.10\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.2\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.4\n      - pytest-cov==6.0.0\n      - requests==2.32.3\n      - six==1.17.0\n      - snowballstemmer==2.2.0\n      - tomli==2.2.1\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - typed-ast==1.5.5\n      - urllib3==2.3.0\n      - virtualenv==20.28.1\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-8548": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-8551": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-8593": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-8595": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-8621": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.11.26=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.21=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.12.14\n      - chardet==5.2.0\n      - charset-normalizer==3.4.1\n      - colorama==0.4.6\n      - coverage==7.6.10\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.2\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.4\n      - pytest-cov==6.0.0\n      - requests==2.32.3\n      - six==1.17.0\n      - snowballstemmer==2.2.0\n      - tomli==2.2.1\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - urllib3==2.3.0\n      - virtualenv==20.28.1\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-8638": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-8721": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.21.2\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
    "sphinx-doc__sphinx-9711": "name: testbed\nchannels:\n  - defaults\n  - conda-forge\ndependencies:\n  - _libgcc_mutex=0.1=main\n  - _openmp_mutex=5.1=1_gnu\n  - ca-certificates=2024.9.24=h06a4308_0\n  - ld_impl_linux-64=2.40=h12ee557_0\n  - libffi=3.4.4=h6a678d5_1\n  - libgcc-ng=11.2.0=h1234567_1\n  - libgomp=11.2.0=h1234567_1\n  - libstdcxx-ng=11.2.0=h1234567_1\n  - ncurses=6.4=h6a678d5_0\n  - openssl=3.0.15=h5eee18b_0\n  - pip=24.2=py39h06a4308_0\n  - python=3.9.20=he870216_1\n  - readline=8.2=h5eee18b_0\n  - setuptools=75.1.0=py39h06a4308_0\n  - sqlite=3.45.3=h5eee18b_0\n  - tk=8.6.14=h39e8969_0\n  - tzdata=2024b=h04d1e81_0\n  - wheel=0.44.0=py39h06a4308_0\n  - xz=5.4.6=h5eee18b_1\n  - zlib=1.2.13=h5eee18b_1\n  - pip:\n      - alabaster==0.7.11\n      - babel==2.16.0\n      - cachetools==5.5.0\n      - certifi==2024.8.30\n      - chardet==5.2.0\n      - charset-normalizer==3.4.0\n      - colorama==0.4.6\n      - coverage==7.6.4\n      - cython==3.0.11\n      - distlib==0.3.9\n      - docutils==0.17.1\n      - exceptiongroup==1.2.2\n      - filelock==3.16.1\n      - html5lib==1.1\n      - idna==3.10\n      - imagesize==1.4.1\n      - iniconfig==2.0.0\n      - jinja2==2.11.3\n      - markupsafe==2.0.1\n      - packaging==24.1\n      - platformdirs==4.3.6\n      - pluggy==1.5.0\n      - pygments==2.18.0\n      - pyproject-api==1.8.0\n      - pytest==8.3.3\n      - pytest-cov==5.0.0\n      - requests==2.32.3\n      - six==1.16.0\n      - snowballstemmer==2.2.0\n      - tomli==2.0.2\n      - tox==4.16.0\n      - tox-current-env==0.0.11\n      - urllib3==2.2.3\n      - virtualenv==20.26.6\n      - webencodings==0.5.1\nprefix: /opt/miniconda3/envs/testbed",
}
