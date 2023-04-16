from .diff import build_diff_tree, get_first_keys
from .reader import read_file
from gendiff.formatters.formatter import call_formatter


__all__ = (
    'generate_diff',
)


def generate_diff(file_path1, file_path2, formatter):
    file1 = read_file(file_path1)
    file2 = read_file(file_path2)
    if file1 is None or file2 is None:
        return
    keys = get_first_keys(file1, file2)
    if (format_func := call_formatter(formatter)) is None:
        return
    return format_func(build_diff_tree(keys, file1, file2))
