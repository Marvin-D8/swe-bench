from pathlib import Path

# Constants - Image Build Directories
BASE_IMAGE_BUILD_DIR = Path("logs/build_images/base")
ENV_IMAGE_BUILD_DIR = Path("logs/build_images/env")
INSTANCE_IMAGE_BUILD_DIR = Path("logs/build_images/instances")

# Constants - Docker Image Building
CONTAINER_USER = "root"
CONTAINER_WORKDIR = "/testbed"

# Constants - Installation Logging
INSTALL_FAIL = ">>>>> Init Failed"
INSTALL_PASS = ">>>>> Init Succeeded" 
INSTALL_TIMEOUT = ">>>>> Init Timed Out"

# Constants - Docker Specifications
DEFAULT_DOCKER_SPECS = {
    "conda_version": "py311_23.11.0-2",
    "node_version": "21.6.2", 
    "pnpm_version": "9.5.0",
    "python_version": "3.9",
    "ubuntu_version": "22.04",
}

# Constants - Image Tags and Architecture
LATEST = "latest"
