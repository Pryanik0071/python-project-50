from .stylish import get_stylish_diff
from .plain import get_plain_diff


def call_formatter(formatter):
    if formatter == 'stylish':
        return get_stylish_diff
    if formatter == 'plain':
        return get_plain_diff
    if formatter == 'json':
        return True
