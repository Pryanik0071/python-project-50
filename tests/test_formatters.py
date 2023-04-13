import pytest

from gendiff.formatters.formatter import call_formatter


@pytest.mark.parametrize("formatter, expected", [
    ('stylish', True),
    ('plain', True),
    ('json', True),
    ('another', False)
])
def test_formatter(formatter, expected):
    assert bool(call_formatter(formatter)) == expected
