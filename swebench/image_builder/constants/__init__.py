from pathlib import Path

IMAGE_BUILDER_LOG_DIR = Path("logs/image_builder")

# Constants - Docker Image Building
CONTAINER_USER = "root"
CONTAINER_WORKDIR = "/testbed"
CONTAINER_ENV_NAME = "testbed"

# Constants - Installation Logging
INSTALL_FAIL = ">>>>> Init Failed"
INSTALL_PASS = ">>>>> Init Succeeded"
INSTALL_TIMEOUT = ">>>>> Init Timed Out"
