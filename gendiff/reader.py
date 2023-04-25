import json
import pathlib

import yaml


def read_json(file_path):
    file_data = dict()
    try:
        file_data = json.load(open(file_path))
    except json.decoder.JSONDecodeError:
        print(f'File {file_path} is empty!')
    return file_data


def read_yaml(file_path):
    with open(file_path) as f:
        file_data = yaml.load(f, Loader=yaml.loader.SafeLoader)
    if file_data is None:
        return dict()
    return file_data


def read_file(file_path):
    if pathlib.Path(file_path).suffix == '.json':
        return read_json(file_path)
    elif pathlib.Path(file_path).suffix in ('.yaml', '.yml'):
        return read_yaml(file_path)
    print('File extension does\'t support, use .json or .yaml/.yml')
