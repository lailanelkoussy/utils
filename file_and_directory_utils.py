
from os import listdir, makedirs
from os.path import isfile, join, isdir, exists
import json

def list_all_files_subpaths(path: str) -> list[str]:
    """
    Args:
        path: string path indicating directory

    Returns: list of all files in *path* directory

    """
    list_elements = []
    for element in listdir(path):
        if isfile(join(path, element)):
            list_elements.append(join(path, element))
        if isdir(join(path, element)):
            list_elements += list_all_files_subpaths(join(path, element))
    return list_elements


def open_all_jsons_path(path: str) -> list[dict]:
    """
    Args:
        path: path containing jsons (even in child directories)

    Returns: list of all jsons inside path (even in sub directories)

    """
    list_elements = []
    for element in listdir(path):
        if isfile(join(path, element)):
            file = open(join(path, element))
            list_elements.append(json.load(file))
        if isdir(join(path, element)):
            list_elements += open_all_jsons_path(join(path, element))
    return list_elements