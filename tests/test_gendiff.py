import pytest

from gendiff import generate_diff


PATH = 'tests/fixtures/'


@pytest.mark.parametrize("file_path1, file_path2, formatter, expected", [
    (PATH + 'file1.json', PATH + 'file2.json', 'stylish', PATH + 'stylish12.txt'),
    (PATH + 'file1.json', PATH + 'file2.yaml', 'stylish', PATH + 'stylish12.txt'),
    (PATH + 'file1.yaml', PATH + 'file2.yml', 'stylish', PATH + 'stylish12.txt'),
    (PATH + 'file1.yaml', PATH + 'file2.json', 'stylish', PATH + 'stylish12.txt'),
    (PATH + 'file3.json', PATH + 'file4.json', 'stylish', PATH + 'stylish34.txt'),
    (PATH + 'file0.json', PATH + 'file1.json', 'stylish', PATH + 'stylish01.txt'),
    (PATH + 'file2.json', PATH + 'file_empty.yml', 'stylish', PATH + 'stylish2zero.txt'),
])
def test_generate_diff(file_path1, file_path2, formatter, expected):
    assert generate_diff(file_path1, file_path2, formatter) == \
           open(expected).read()


@pytest.mark.parametrize("file_path1, file_path2, formatter, expected", [
    (PATH + 'file1.txt', PATH + 'file2.json', 'stylish', None),
    (PATH + 'file1.json', PATH + 'file1.txt', 'stylish', None)
])
def test_gendiff_wrong_extension(file_path1, file_path2, formatter, expected):
    assert generate_diff(file_path1, file_path2, formatter) == expected


def test_gendiff_wrong_formatter():
    assert generate_diff(PATH + 'file1.json', PATH + 'file2.json', 'some') is None
