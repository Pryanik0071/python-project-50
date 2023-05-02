INDENT = 4


def get_status(status_):
    if status_ in {'UNCHANGED', 'NESTED'}:
        return '    '
    if status_ == 'ADDED':
        return '  + '
    return '  - '


def get_space(deep):
    return ' ' * (INDENT * deep - 4)


def transform_value(value_):
    if isinstance(value_, bool) or value_ is None:
        return {
            False: 'false',
            True: 'true',
            None: 'null',
        }.get(value_)
    return str(value_)


def get_head(deep, status, dict_):
    return f'{get_space(deep)}{get_status(status)}{dict_["key"]}: '


def calculate_value(val, deep):
    if isinstance(val, dict):
        if len(val) == 1:
            key, value = list(val.items())[0]
            return f'{"{"}\n{get_space(deep + 1)}{key}: ' \
                   f'{calculate_value(value, deep + 1)}' \
                   f'\n{get_space(deep)}{"}"}'
        list_ = []
        for key, values in val.items():
            list_.append(f'\n{get_space(deep + 1)}{key}: '
                         f'{calculate_value(values, deep + 1)}')
        return f'{"{"}{"".join(list_)}\n{get_space(deep)}{"}"}'
    return transform_value(val)


def build_stylish_tree(dict_, deep):
    status = dict_.get('status')
    if status != 'CHANGED':
        key = get_head(deep, status, dict_)
        if status == 'NESTED':
            result = '\n'.join(list(map(
                lambda x: build_stylish_tree(x, deep + 1), dict_['value'])))
            value = f'{"{"}\n{result}\n{get_space(deep + 1)}{"}"}'
            return key + value
        value = calculate_value(dict_['value'], deep + 1)
        return key + value
    k_old = get_head(deep, '', dict_)
    val_old = calculate_value(dict_['value_old'], deep + 1)
    k_new = '\n' + get_head(deep, 'ADDED', dict_)
    val_new = calculate_value(dict_['value_new'], deep + 1)
    return k_old + val_old + k_new + val_new


def get_stylish_diff(node):
    list_ = []
    for children in node:
        list_.append(build_stylish_tree(children, 1))
    return '{\n' + '\n'.join(list_) + '\n}'
