import json

import pytest
import yaml

from .fixtures import objects as obj
from gendiff.diff import build_diff_tree, get_first_keys


PATH = 'tests/fixtures/'


@pytest.mark.parametrize("obj1, obj2, expected", [
    (obj.file1, obj.file2, obj.keys12),
    (obj.file1, {}, obj.keys10),
    ({}, obj.file2, obj.keys02),
])
def test_keys(obj1, obj2, expected):
    assert get_first_keys(obj1, obj2) == expected


@pytest.mark.parametrize("obj1, obj2, expected", [
    (obj.file1, obj.file2, obj.diff12)
])
def test_diff(obj1, obj2, expected):
    keys = sorted(set(list(obj1.keys()) + list(obj2.keys())))
    assert build_diff_tree(keys, obj1, obj2) == expected


@pytest.mark.parametrize("file_path1, file_path2, expected", [
    (PATH + 'file1.json', PATH + 'file2.json', PATH + 'diff_1_2.txt'),
    (PATH + 'file3.json', PATH + 'file4.json', PATH + 'diff_3_4.txt'),

])
def test_diff_json(file_path1, file_path2, expected):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    keys = sorted(set(list(file1.keys()) + list(file2.keys())))
    assert f'{build_diff_tree(keys, file1, file2)}' == \
           open(expected).read().rstrip()


@pytest.mark.parametrize("file_path1, file_path2, expected", [
    (PATH + 'file1.yaml', PATH + 'file2.yml', PATH + 'diff_1_2.txt'),
    (PATH + 'file1.yml', PATH + 'file2.yaml', PATH + 'diff_1_2.txt'),
])
def test_diff_yaml(file_path1, file_path2, expected):
    with open(file_path1) as file1:
        file1 = yaml.load(file1, Loader=yaml.loader.SafeLoader)
    with open(file_path2) as file2:
        file2 = yaml.load(file2, Loader=yaml.loader.SafeLoader)
    keys = sorted(set(list(file1.keys()) + list(file2.keys())))
    assert f'{build_diff_tree(keys, file1, file2)}' == \
           open(expected).read().rstrip()


@pytest.mark.parametrize("file_path1, file_path2, expected", [
    (PATH + 'file1.json', PATH + 'file2.yml', PATH + 'diff_1_2.txt'),
    (PATH + 'file1.json', PATH + 'file2.yaml', PATH + 'diff_1_2.txt'),
])
def test_diff_json_yaml(file_path1, file_path2, expected):
    file1 = json.load(open(file_path1))
    with open(file_path2) as file2:
        file2 = yaml.load(file2, Loader=yaml.loader.SafeLoader)
    keys = sorted(set(list(file1.keys()) + list(file2.keys())))
    assert f'{build_diff_tree(keys, file1, file2)}' == \
           open(expected).read().rstrip()


@pytest.mark.parametrize("file_path1, file_path2, expected", [
    (PATH + 'file1.yaml', PATH + 'file2.json', PATH + 'diff_1_2.txt'),
    (PATH + 'file1.yml', PATH + 'file2.json', PATH + 'diff_1_2.txt'),
])
def test_diff_yaml_json(file_path1, file_path2, expected):
    with open(file_path1) as file1:
        file1 = yaml.load(file1, Loader=yaml.loader.SafeLoader)
    file2 = json.load(open(file_path2))
    keys = sorted(set(list(file1.keys()) + list(file2.keys())))
    assert f'{build_diff_tree(keys, file1, file2)}' == \
           open(expected).read().rstrip()
