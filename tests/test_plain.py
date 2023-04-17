import pytest

from .fixtures import objects as obj
from gendiff.formatters.plain import (
    get_value,
    get_plain_diff
)


PATH = 'tests/fixtures/'


@pytest.mark.parametrize("value, expected", [
    ('', "''"),
    (False, 'false'),
    (True, 'true'),
    (None, 'null'),
    ('some_string', '\'some_string\''),
    ({'key': 'value'}, '[complex value]')
])
def test_transform_value(value, expected):
    assert get_value(value) == expected


@pytest.mark.parametrize("value, expected", [
    (obj.diff34, PATH + 'plain34.txt'),
    # (obj.diff12, PATH + 'stylish12.txt'),
])
def test_get_stylish_diff(value, expected):
    assert get_plain_diff(value) == open(expected).read()
