def get_status(status_):
    if status_ == 'STAY':
        return '    '
    if status_ == 'ADD':
        return '  + '
    return '  - '


def get_space(deep):
    return " " * 4 * deep


def transform_value(value_):
    if isinstance(value_, bool) or value_ is None:
        return {
            False: ' false',
            True: ' true',
            None: ' null',
        }.get(value_)
    if value_ == '':
        return ''
    return f' {value_}'


def get_head(deep, status, dict_):
    return f'{get_space(deep)}{get_status(status)}{dict_["key"]}:'


def calculate_value(val, deep):
    if isinstance(val, dict):
        if len(val) == 1:
            key, value = list(val.items())[0]
            return ' {\n' + f'{get_space(deep + 1)}{key}:' \
                            f'{calculate_value(value, deep + 1)}' \
                + f'\n{get_space(deep)}' + '}'
        list_ = []
        for key, values in val.items():
            list_.append(f'\n{get_space(deep + 1)}{key}:'
                         f'{calculate_value(values, deep + 1)}')
        return ' {' + ''.join(list_) + f'\n{get_space(deep)}' + '}'
    return transform_value(val)


def build_stylish_tree(dict_, deep):
    if dict_.get('status') != 'CHANGE':
        if isinstance(dict_['value'], list):
            result = '\n'.join(list(map(
                lambda x: build_stylish_tree(x, deep + 1), dict_['value'])))
            return get_head(deep, dict_["status"], dict_) + \
                ' {' + f'\n{result}' + f'\n{get_space(deep + 1)}' + '}'
        return get_head(deep, dict_["status"], dict_) + \
            calculate_value(dict_["value"], deep + 1)
    return get_head(deep, "", dict_) + \
        calculate_value(dict_["value1_old"], deep + 1) + \
        '\n' + get_head(deep, "ADD", dict_) + \
        f'{calculate_value(dict_["value2_new"], deep + 1)}'


def get_stylish_diff(node):
    list_ = []
    for _ in node:
        list_.append(build_stylish_tree(_, 0))
    return '{\n' + '\n'.join(list_) + '\n}'
