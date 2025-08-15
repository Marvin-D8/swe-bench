import logging
import sys
from pathlib import Path


def setup_logger(instance_id: str, log_file: Path, mode="w", add_stdout: bool = False):
    """
    Set up a logger for evaluation and build processes.
    
    This logger is used for logging the evaluation process, build process of images and containers,
    and other operations that require file-based logging with optional console output.
    It writes logs to the specified log file.

    If `add_stdout` is True, logs will also be sent to stdout, which can be used for
    streaming ephemeral output from Modal containers or other real-time monitoring needs.
    
    Args:
        instance_id: Unique identifier for the instance being processed
        log_file: Path to the log file where logs will be written
        mode: File mode for opening the log file (default: "w")
        add_stdout: Whether to also output logs to stdout (default: False)
    
    Returns:
        logging.Logger: Configured logger instance with log_file attribute
    """
    log_file.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(f"{instance_id}.{log_file.name}")
    handler = logging.FileHandler(log_file, mode=mode, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    setattr(logger, "log_file", log_file)
    if add_stdout:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            f"%(asctime)s - {instance_id} - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger


def close_logger(logger):
    """
    Close all handlers associated with a logger and remove them.
    
    Args:
        logger: The logger instance to close
    """
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)
