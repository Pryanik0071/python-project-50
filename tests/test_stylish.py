import pytest

from .fixtures import objects as obj
from gendiff.formatters.stylish import (
    get_status,
    get_space,
    transform_value,
    get_stylish_diff
)


PATH = 'tests/fixtures/'


@pytest.mark.parametrize('status, expected', [
    ('STAY', '    '),
    ('ADD', '  + '),
    ('DEL', '  - ')
])
def test_get_status(status, expected):
    assert get_status(status) == expected


@pytest.mark.parametrize('deep, expected', [
    (0, ""),
    (1, "    ")
])
def test_get_space(deep, expected):
    assert get_space(deep) == expected


@pytest.mark.parametrize('value, expected', [
    ('', ""),
    (False, ' false'),
    (True, ' true'),
    (None, ' null'),
    ('some_string', ' some_string')
])
def test_transform_value(value, expected):
    assert transform_value(value) == expected


@pytest.mark.parametrize('value, expected', [
    (obj.diff34, PATH + 'stylish34.txt'),
    (obj.diff12, PATH + 'stylish12.txt'),
])
def test_get_stylish_diff(value, expected):
    assert get_stylish_diff(value) == open(expected).read()
