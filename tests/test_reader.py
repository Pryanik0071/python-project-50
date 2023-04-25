import pytest

from .fixtures import objects as obj
from gendiff.reader import read_file


PATH = 'tests/fixtures/'


@pytest.mark.parametrize('file_path, expected', [
    (PATH + 'file1.json', obj.file1),
    (PATH + 'file1.yaml', obj.file1),
    (PATH + 'file1.yml', obj.file1),
    (PATH + 'file1.txt', None),
    (PATH + 'file0.json', {}),
    (PATH + 'file_empty.json', {}),
    (PATH + 'file_empty.yml', {}),
])
def test_reader(file_path, expected):
    assert read_file(file_path) == expected
