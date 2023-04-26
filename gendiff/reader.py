import json
import pathlib

import yaml


def read_json(file_path):
    with open(file_path) as f:
        file_data = json.load(f)
    return file_data


def read_yaml(file_path):
    with open(file_path) as f:
        file_data = yaml.load(f, Loader=yaml.loader.SafeLoader)
    return file_data


def read_file(file_path):
    if pathlib.Path(file_path).suffix == '.json':
        return read_json(file_path)
    if pathlib.Path(file_path).suffix in ('.yaml', '.yml'):
        return read_yaml(file_path)
    print('File extension does\'t support, use .json or .yaml/.yml')
