from .stylish_formatter import get_stylish_diff
from .plain_formatter import get_plain_diff
from .json_formatter import get_json


def get_formatter(formatter):
    if formatter == 'stylish':
        return get_stylish_diff
    if formatter == 'plain':
        return get_plain_diff
    if formatter == 'json':
        return get_json
