import json
import pathlib

import yaml


def read_file(file_path):
    if pathlib.Path(file_path).suffix == '.json':
        return json.load(open(file_path))
    elif pathlib.Path(file_path).suffix in ('.yaml', '.yml'):
        with open(file_path) as f:
            return yaml.load(f, Loader=yaml.loader.SafeLoader)
    print('File extension does\'t support, use .json or .yaml/.yml')
