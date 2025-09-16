from __future__ import annotations

import docker
import docker.errors
import traceback


def _get_log_objects(logger):
    if not logger:
        # if logger is None, print to stdout
        log_info = print
        log_error = print
        raise_error = True
    elif logger == "quiet":
        # if logger is "quiet", don't print anything
        log_info = lambda x: None
        log_error = lambda x: None
        raise_error = True
    else:
        # if logger is a logger object, use it
        log_info = logger.info
        log_error = logger.info
        raise_error = False
    return (log_info, log_error, raise_error)


def remove_image(client, image_id, logger=None):
    """
    Remove a Docker image by ID.

    Args:
        client (docker.DockerClient): Docker client.
        image_id (str): Image ID.
        logger (logging.Logger): Logger to use for output. If None, print to stdout.
    """
    log_info, log_error, raise_error = _get_log_objects(logger)
    try:
        log_info(f"Attempting to remove image {image_id}...")
        client.images.remove(image_id, force=True)
        log_info(f"Image {image_id} removed.")
    except docker.errors.ImageNotFound:
        log_info(f"Image {image_id} not found, removing has no effect.")
    except Exception as e:
        if raise_error:
            raise e
        log_error(f"Failed to remove image {image_id}: {e}\n{traceback.format_exc()}")
