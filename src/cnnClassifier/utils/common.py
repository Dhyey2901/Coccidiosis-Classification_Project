import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox           #we used configbox because it becomes easier to access each element
from pathlib import Path
from typing import Any
import base64



@ensure_annotations                     #this
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    Args:
        path_to_yaml (str): path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
         ConfigBox: ConfigBox type.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        return ValueError("Yaml File is empty")
    except Exception as e:
        raise e




@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    create a list of directories
    :param path_to_directories: list of path of directories
            ignorel_log(bool,optional): ignore if multiple dirs is to be created. Defaults to false.

    """

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at path: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """

    :param path: path to json file
    :param data: Data to be saved in json file
    :return:
    """
    with open(path, "w") as f:
        json.dumps(data,f,indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """

    :param path: Path to json file
    :return: ConfigBox: data as class attributes instead of dict
    """

    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    save binary file

    :param data: data to be saved as binary
    :param path: path where the binary data will be stored
    :return:
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path):
    """

    :param path: path to binary file
    :return: Any: object stored in file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded successfully from : {path}")
    return data

@ensure_annotations
def get_size(path:Path):
    """
    get the size of file in KB
    :param path: path of the file
    :return: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

def decodeImage(imgstring,fileName):
    imgData = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgData)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,"rb") as f:
        return base64.b64decode(f.read())