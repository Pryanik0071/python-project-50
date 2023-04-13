import pytest

from gendiff.reader import read_file


PATH = 'tests/fixtures/'


@pytest.mark.parametrize("file_path, expected", [
    (PATH + 'file1.json', True),
    (PATH + 'file1.yaml', True),
    (PATH + 'file1.yml', True),
    (PATH + 'file1.txt', False)
])
def test_reader(file_path, expected):
    assert bool(read_file(file_path)) == expected
