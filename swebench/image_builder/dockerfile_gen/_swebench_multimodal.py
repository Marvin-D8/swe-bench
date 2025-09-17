_DOCKERFILE_BASE_JS = r"""
FROM --platform=linux/amd64 ubuntu:jammy

ARG DEBIAN_FRONTEND=noninteractive

ENV TZ=Etc/UTC

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    libssl-dev \
    software-properties-common \
    wget \
    gnupg \
    jq \
    ca-certificates \
    dbus \
    ffmpeg \
    imagemagick \
    && apt-get -y autoclean \
    && rm -rf /var/lib/apt/lists/*
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg \
        fonts-khmeros fonts-kacst fonts-freefont-ttf libxss1 dbus dbus-x11 \
        --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

ENV NVM_DIR /usr/local/nvm

RUN mkdir -p $NVM_DIR
RUN curl --silent -o- https://raw.githubusercontent.com/creationix/nvm/v0.39.3/install.sh | bash
RUN apt-get update && apt-get install -y \
    procps \
    libasound2 libatk-bridge2.0-0 libatk1.0-0 libcups2 libdrm2 \
    libgbm1 libgconf-2-4 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 \
    libnss3 libpango-1.0-0 libpangocairo-1.0-0 libxcomposite1 \
    libxdamage1 libxfixes3 libxkbcommon0 libxrandr2 libxss1 libxshmfence1 libglu1 \
    && apt-get -y autoclean \
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN /usr/bin/google-chrome
RUN echo "CHROME_BIN=$CHROME_BIN" >> /etc/environment
RUN mkdir -p /run/dbus

ENV DBUS_SESSION_BUS_ADDRESS="unix:path=/run/dbus/system_bus_socket"

RUN dbus-daemon --system --fork

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
ENV OPENSSL_CONF /etc/ssl

RUN useradd -m chromeuser

USER chromeuser

WORKDIR /home/chromeuser

USER root
"""

from swebench.data_specs.javascript import MAP_REPO_VERSION_TO_SPECS_JS


def make_heredoc_run_command(commands):
    """Helper to create RUN commands with heredoc syntax"""
    if not commands:
        return ""
    delimiter = "EOF"
    command_str = "\n".join(commands)
    return f"RUN <<{delimiter}\n{command_str}\n{delimiter}"


def make_repo_script_list(specs, repo, base_commit):
    """
    Clone the repository and set up the codebase.
    """
    commands = [
        f"git clone https://github.com/{repo}.git /testbed",
        "cd /testbed",
        f"git reset --hard {base_commit}",
        "git clean -fdxq",
    ]
    return make_heredoc_run_command(commands)


def make_env_script_list(instance, specs):
    """
    Set up the JavaScript/Node.js environment with required dependencies.
    """
    commands = []

    # Install additional apt packages if specified
    if "apt-pkgs" in specs:
        apt_packages = " ".join(specs["apt-pkgs"])
        commands.extend(
            [
                "apt-get update",
                f"apt-get install -y {apt_packages}",
                "rm -rf /var/lib/apt/lists/*",
            ]
        )

    # Set up Node.js version from docker_specs
    docker_specs = specs.get("docker_specs", {})
    node_version = docker_specs.get("node_version", "18.17.1")  # default fallback
    pnpm_version = docker_specs.get("pnpm_version", "8.6.12")  # default fallback
    python_version = docker_specs.get("python_version", "3.9")  # default fallback

    # Install Node.js
    commands.extend(
        [
            f"export NODE_VERSION={node_version}",
            "source $NVM_DIR/nvm.sh",
            "nvm install $NODE_VERSION",
            "nvm alias default $NODE_VERSION",
            "nvm use default",
        ]
    )

    # Set environment variables
    commands.extend(
        [
            f"export NODE_PATH=$NVM_DIR/v{node_version}/lib/node_modules",
            f"export PATH=$NVM_DIR/versions/node/v{node_version}/bin:$PATH",
        ]
    )

    # Install pnpm if specified
    if "pnpm_version" in docker_specs:
        commands.extend(
            [
                f"export PNPM_VERSION={pnpm_version}",
                "export PNPM_HOME=/usr/local/pnpm",
                "export PATH=$PNPM_HOME:$PATH",
                "mkdir -p $PNPM_HOME",
                'wget -qO $PNPM_HOME/pnpm "https://github.com/pnpm/pnpm/releases/download/v$PNPM_VERSION/pnpm-linux-x64"',
                "chmod +x $PNPM_HOME/pnpm",
                "ln -s $PNPM_HOME/pnpm /usr/local/bin/pnpm",
            ]
        )

    # Install Python if needed
    commands.extend(
        [
            "add-apt-repository ppa:deadsnakes/ppa",
            "apt-get update",
            f"apt-get install -y python{python_version}",
            f"ln -sf /usr/bin/python{python_version} /usr/bin/python",
        ]
    )

    return make_heredoc_run_command(commands)


def _get_dockerfile(instance) -> str:
    """
    Generate a monolithic Dockerfile for SWE-bench Multimodal instances.
    This combines the base image, environment setup, and repository setup into a single Dockerfile.
    """
    repo = instance["repo"]
    version = instance.get("version")
    base_commit = instance["base_commit"]
    specs = MAP_REPO_VERSION_TO_SPECS_JS[repo][version]
    dockerfile = _DOCKERFILE_BASE_JS
    env_script = make_env_script_list(instance, specs)
    if env_script:
        dockerfile += f"\n{env_script}\n"
    repo_script = make_repo_script_list(specs, repo, base_commit)
    if repo_script:
        dockerfile += f"\n{repo_script}\n"
    dockerfile += "\nWORKDIR /testbed/\n"
    return dockerfile
