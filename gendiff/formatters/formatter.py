from .stylish import get_stylish_diff


def call_formatter(formatter):
    if formatter == 'stylish':
        return get_stylish_diff
    if formatter == 'plain':
        return True
    if formatter == 'json':
        return True
