def get_head(key):
    return f'Property \'{key}\' was '


def get_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool) or value is None:
        return {
            False: 'false',
            True: 'true',
            None: 'null',
        }.get(value)
    return f'\'{value}\''


def build_plain_tree(dict_, keys):
    key = keys + dict_["key"]
    if dict_.get('status') != 'CHANGE':
        if isinstance(dict_['value'], list):
            return '\n'.join(list(map(lambda x: build_plain_tree(
                x, key + '.'), dict_['value'])))
        if dict_.get('status') == 'ADD':
            value = get_value(dict_["value"])
            return get_head(key) + f'added with value: {value}'
        elif dict_.get('status') == 'DEL':
            return get_head(key) + 'removed'
        return ''
    value_old = get_value(dict_["value1_old"])
    value_new = get_value(dict_["value2_new"])
    return get_head(key) + f'updated. From {value_old} to {value_new}'


def get_plain_diff(node):
    list_ = []
    for _ in node:
        list_.append(build_plain_tree(_, ''))
    return '\n'.join(list_).replace('\n\n', '\n')