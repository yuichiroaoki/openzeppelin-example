import os
from os.path import join, isdir
from pathlib import Path


def file_extension(file):
    try:
        return Path(file).suffix
    except:
        return ""


def list_files(file_type):
    folderPath = Path(f"./")
    onlyfiles = [f for f in folderPath.iterdir() if f.is_file()]
    if file_type:
        onlyfiles = [f for f in onlyfiles if file_type == file_extension(f)]
    return onlyfiles


def list_folders(folder_name):
    folderPath = "./" + folder_name
    onlyfolders = [f for f in os.listdir(
        folderPath) if isdir(join(folderPath, f))]
    return onlyfolders


def create_folder_if_not_exist(path: str, folder_name: str) -> None:
    if not folder_name in list_folders(path):
        Path(f'{path}/{folder_name}').mkdir(parents=True)
