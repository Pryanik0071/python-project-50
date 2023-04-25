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
    if isinstance(value, int):
        return value
    return f'\'{value}\''


def build_plain_tree(dict_, keys):
    status = dict_.get('status')
    key = keys + dict_['key']
    if status != 'CHANGED':
        if status == 'NESTED':
            return '\n'.join(list(map(lambda x: build_plain_tree(
                x, key + '.'), dict_['value'])))
        if status == 'ADDED':
            value = get_value(dict_['value'])
            return get_head(key) + f'added with value: {value}'
        if status == 'DELETED':
            return get_head(key) + 'removed'
        return ''
    value_old = get_value(dict_['value_old'])
    value_new = get_value(dict_['value_new'])
    return get_head(key) + f'updated. From {value_old} to {value_new}'


def get_plain_diff(node):
    list_ = []
    for _ in node:
        list_.append(build_plain_tree(_, ''))
    return '\n'.join(list_).replace('\n\n', '\n')
