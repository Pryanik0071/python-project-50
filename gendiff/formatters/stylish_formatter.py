INDENT = 4


def get_status(status_):
    if status_ in {'UNCHANGED', 'NESTED'}:
        return '    '
    if status_ == 'ADDED':
        return '  + '
    return '  - '


def get_space(depth):
    return ' ' * (INDENT * depth - 4)


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
    if status != 'CHANGED':
        key = get_head(depth, status, dict_)
        if status == 'NESTED':
            result = '\n'.join(list(map(
                lambda x: build_stylish_tree(x, depth + 1), dict_['value'])))
            value = f'{"{"}\n{result}\n{get_space(depth + 1)}{"}"}'
            return key + value
        value = calculate_value(dict_['value'], depth + 1)
        return key + value
    k_old = get_head(depth, '', dict_)
    val_old = calculate_value(dict_['value_old'], depth + 1)
    k_new = '\n' + get_head(depth, 'ADDED', dict_)
    val_new = calculate_value(dict_['value_new'], depth + 1)
    return k_old + val_old + k_new + val_new


def get_stylish_diff(node):
    list_ = []
    for children in node:
        list_.append(build_stylish_tree(children, 1))
    return '{\n' + '\n'.join(list_) + '\n}'
