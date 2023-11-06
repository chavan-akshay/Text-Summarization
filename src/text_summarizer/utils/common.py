import os
from box.exceptions import BoxValueError
import yaml
from src.text_summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations    # Responsible to check the data type of the input data and if not corret then raise an error.
def read_yaml(path_to_yaml: Path) -> ConfigBox:  # Here ConfigBox object (datatype) is returned.
    """
    Read the yaml file and return a ConfigBox object.

    Parameters
    ----------
    path_to_yaml : Path
        Path to the yaml file.

    Raises:
        ValueError: if yaml file is empty
        e: empty yaml file

    Returns
    -------
    ConfigBox
        A ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        logger.error(f"yaml file: {path_to_yaml} not loaded successfully")
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories.

    Parameters
    ----------
    path_to_directories : list
        List of paths of directories.
    ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in kb.

    Parameters
    ----------
    path : Path
        Path to the file.

    Returns
    -------
    str
        Size of the file in kb.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} kb"
