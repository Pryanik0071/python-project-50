import pytest

from .fixtures import objects as obj
from gendiff.formatters.json_formatter import get_json


PATH = 'tests/fixtures/'


@pytest.mark.parametrize('value, expected', [
    (obj.diff34, PATH + 'json_formatter.txt')
])
def test_get_json_diff(value, expected):
    assert get_json(value) == open(expected).read()