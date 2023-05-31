import pytest

from gendiff import generate_diff


PATH = 'tests/fixtures/'


@pytest.mark.parametrize('file_path1, file_path2, formatter, expected', [
    (f'{PATH}file1.json', f'{PATH}file2.yaml', 'stylish', f'{PATH}stylish12.txt'),
    (f'{PATH}file1.yaml', f'{PATH}file2.yml', 'stylish', f'{PATH}stylish12.txt'),
    (f'{PATH}file3.json', f'{PATH}file4.json', 'stylish', f'{PATH}stylish34.txt'),
    (f'{PATH}file0.json', f'{PATH}file1.json', 'stylish', f'{PATH}stylish01.txt'),
    (f'{PATH}file3.json', f'{PATH}file4.json', 'plain', f'{PATH}plain34.txt'),
    (f'{PATH}file3.json', f'{PATH}file4.json', 'json', f'{PATH}json34.txt'),
])
def test_generate_diff(file_path1, file_path2, formatter, expected):
    with open(expected) as f:
        expected_out = f.read()
    assert generate_diff(file_path1, file_path2, formatter) == expected_out


def test_gendiff_wrong_formatter():
    assert generate_diff(f'{PATH}file1.json', f'{PATH}file2.json', 'some') is None
