"""
SWE-bench Image Builder

This module handles Docker image building for SWE-bench instances.
It provides functionality to build base, environment, and instance images
required for evaluation.
"""

from swebench.image_builder.image_spec import ImageSpec, make_image_spec, get_image_specs_from_dataset
from swebench.image_builder.docker_build import (
    build_instance_image,
    build_instance_images,
    BuildImageError,
)
from swebench.image_builder.docker_utils import (
    cleanup_container,
    copy_to_container,
    exec_run_with_timeout,
    list_images,
    remove_image,
    clean_images,
)

__all__ = [
    "ImageSpec",
    "make_image_spec",
    "get_image_specs_from_dataset",
    "build_base_images",
    "build_env_images",
    "build_instance_images", 
    "build_instance_image",
    "BuildImageError",
    "cleanup_container",
    "copy_to_container",
    "exec_run_with_timeout",
    "list_images",
    "remove_image",
    "clean_images",
]