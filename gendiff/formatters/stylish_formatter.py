INDENT = 4


def get_status(status_):
    if status_ in {'UNCHANGED', 'NESTED'}:
        return ' ' * INDENT
    if status_ == 'ADDED':
        return ' ' * (INDENT - 2) + '+ '
    return ' ' * (INDENT - 2) + '- '


def get_space(depth):
    return ' ' * INDENT * depth


def transform_value(value_):
    if isinstance(value_, bool) or value_ is None:
        return {
            False: 'false',
            True: 'true',
            None: 'null',
        }.get(value_)
    return str(value_)


def get_head(depth, status, dict_):
    return f'{get_space(depth)}{get_status(status)}{dict_["key"]}: '


def calculate_value(val, depth):
    if isinstance(val, dict):
        if len(val) == 1:
            key, value = list(val.items())[0]
            return f'{"{"}\n{get_space(depth + 1)}{key}: ' \
                   f'{calculate_value(value, depth + 1)}' \
                   f'\n{get_space(depth)}{"}"}'
        list_ = []
        for key, values in val.items():
            list_.append(f'\n{get_space(depth + 1)}{key}: '
                         f'{calculate_value(values, depth + 1)}')
        return f'{"{"}{"".join(list_)}\n{get_space(depth)}{"}"}'
    return transform_value(val)


def build_stylish_tree(dict_, depth):
    status = dict_.get('status')
    if status == 'CHANGED':
        key_old = get_head(depth, '', dict_)
        value_old = calculate_value(dict_['value_old'], depth + 1)
        key_new = f'\n{get_head(depth, "ADDED", dict_)}'
        value_new = calculate_value(dict_['value_new'], depth + 1)
        return f'{key_old}{value_old}{key_new}{value_new}'
    key = get_head(depth, status, dict_)
    if status == 'NESTED':
        result = '\n'.join(list(map(
            lambda x: build_stylish_tree(x, depth + 1), dict_['value'])))
        value = f'{"{"}\n{result}\n{get_space(depth + 1)}{"}"}'
        return f'{key}{value}'
    value = calculate_value(dict_['value'], depth + 1)
    return f'{key}{value}'  # ADDED DELETED UNCHANGED


def get_stylish_diff(diff):
    result = []
    for children in diff:
        result.append(build_stylish_tree(children, 0))
    out = '\n'.join(result)
    return f'{"{"}\n{out}\n{"}"}'
