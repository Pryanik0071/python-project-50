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


def build_plain_tree(dict_, nested_key):
    status = dict_.get('status')
    key = f'{nested_key}{dict_["key"]}'
    if status == 'CHANGED':
        value_old = get_value(dict_['value_old'])
        value_new = get_value(dict_['value_new'])
        return f'{get_head(key)}updated. From {value_old} to {value_new}'
    if status == 'NESTED':
        return '\n'.join(list(map(lambda x: build_plain_tree(
            x, f'{key}.'), dict_['value'])))
    if status == 'ADDED':
        value = get_value(dict_['value'])
        return f'{get_head(key)}added with value: {value}'
    if status == 'DELETED':
        return f'{get_head(key)}removed'
    return ''


def get_plain_diff(diff):
    list_ = []
    for children in diff:
        list_.append(build_plain_tree(children, ''))
    return '\n'.join(list_).replace('\n\n', '\n')
