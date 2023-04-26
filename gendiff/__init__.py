from .diff import get_diff_tree
from .reader import read_file
from gendiff.formatters.formatter import get_formatter


__all__ = (
    'generate_diff',
)


def generate_diff(file_path1, file_path2, formatter='stylish'):
    file1 = read_file(file_path1)
    file2 = read_file(file_path2)
    if file1 is None or file2 is None:
        return
    if (format_func := get_formatter(formatter)) is None:
        return
    return format_func(get_diff_tree(file1, file2))
