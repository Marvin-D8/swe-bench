import docker
import resource

from argparse import ArgumentParser
from pathlib import Path

from swebench.image_builder.image_spec import load_swebench_dataset_image_specs
from swebench.image_builder.docker_build import build_instance_images
from swebench.image_builder.docker_utils import list_images
from swebench.harness.utils import str2bool, optional_str


def filter_image_specs(
    image_specs: list,
    client: docker.DockerClient,
    force_rebuild: bool,
):
    """
    Filter the dataset to only include instances that need to be built.

    Args:
        dataset (list): List of instances (usually all of SWE-bench dev/test split) with image specs
        client (docker.DockerClient): Docker client.
        force_rebuild (bool): Whether to force rebuild all images.
    """
    # Get existing images
    existing_images = list_images(client)
    data_to_build = []

    for spec in image_specs:
        # Check if the instance needs to be built (based on force_rebuild flag and existing images)
        if force_rebuild:
            data_to_build.append(spec)
        elif spec.name not in existing_images:
            data_to_build.append(spec)

    return data_to_build


def main(
    dataset_name,
    split,
    instance_ids,
    max_workers,
    force_rebuild,
    open_file_limit,
    namespace,
    tag,
    dry_run,
):
    """
    Build Docker images for the specified instances.

    Args:
        instance_ids (list): List of instance IDs to build.
        max_workers (int): Number of workers for parallel processing.
        force_rebuild (bool): Whether to force rebuild all images.
        open_file_limit (int): Open file limit.
        dry_run (bool): If True, create docker files and build contexts but don't build images.
    """
    # Set open file limit
    resource.setrlimit(resource.RLIMIT_NOFILE, (open_file_limit, open_file_limit))
    client = docker.from_env()

    image_specs = load_swebench_dataset_image_specs(dataset_name, split, namespace, tag, instance_ids)
    image_specs = filter_image_specs(
        image_specs, client, force_rebuild
    )

    if len(image_specs) == 0:
        print("All images exist. Nothing left to build.")
        return 0

    if dry_run:
        print(f"DRY RUN MODE: Creating build contexts for {len(image_specs)} images (no actual builds will be performed)")
    
    # Build images for remaining instances
    successful, failed = build_instance_images(
        client=client,
        image_specs=image_specs,
        force_rebuild=force_rebuild,
        max_workers=max_workers,
        dry_run=dry_run,
    )
    if dry_run:
        print(f"Successfully created build contexts for {len(successful)} images")
        if len(failed) > 0:
            print(f"Failed to create build contexts for {len(failed)} images")
    else:
        print(f"Successfully built {len(successful)} images")
        if len(failed) > 0:
            print(f"Failed to build {len(failed)} images")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--dataset_name",
        type=str,
        default="SWE-bench/SWE-bench_Verified",
        help="Name of the dataset to use",
    )
    parser.add_argument("--split", type=str, default="test", help="Split to use")
    parser.add_argument(
        "--instance_ids",
        nargs="+",
        type=str,
        help="Instance IDs to run (space separated)",
    )
    parser.add_argument(
        "--max_workers", type=int, default=4, help="Max workers for parallel processing"
    )
    parser.add_argument(
        "--force_rebuild", type=str2bool, default=False, help="Force rebuild images"
    )
    parser.add_argument(
        "--open_file_limit", type=int, default=8192, help="Open file limit"
    )
    parser.add_argument(
        "--namespace",
        type=optional_str,
        default=None,
        help="Namespace to use for the images (default: None)",
    )
    parser.add_argument(
        "--tag", type=str, default=None, help="Tag to use for the images"
    )
    parser.add_argument(
        "--dry_run", 
        type=str2bool, 
        default=False, 
        help="Create docker files and build contexts but don't build images"
    )
    args = parser.parse_args()
    main(**vars(args))
