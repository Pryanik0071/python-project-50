import json
import os

import yaml


def read_content(file_path):
    with open(file_path) as f:
        content = f.read()
    return content


def read_json(content):
    return json.loads(content)


def read_yaml(content):
    return yaml.load(content, Loader=yaml.loader.SafeLoader)


def parse_content(file_path, content):
    _, extension = os.path.splitext(file_path)
    if extension == '.json':
        return read_json(content)
    if extension in ('.yaml', '.yml'):
        return read_yaml(content)
    print('File extension does\'t support, use .json or .yaml/.yml')


def parse_file(file_path):
    return parse_content(file_path, read_content(file_path))
