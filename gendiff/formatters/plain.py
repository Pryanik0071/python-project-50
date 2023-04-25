diff34 = [
    {'key': 'common', 'status': 'NESTED', 'value': [
        {'key': 'follow', 'status': 'ADD', 'value': False},
        {'key': 'setting1', 'status': 'STAY', 'value': 'Value 1'},
        {'key': 'setting2', 'status': 'DEL', 'value': 200},
        {'key': 'setting3', 'status': 'CHANGE', 'value1_old': True, 'value2_new': None},
        {'key': 'setting4', 'status': 'ADD', 'value': 'blah blah'},
        {'key': 'setting5', 'status': 'ADD', 'value': {'key5': 'value5'}},
        {'key': 'setting6', 'status': 'NESTED', 'value': [
            {'key': 'doge', 'status': 'NESTED', 'value': [
                {'key': 'wow', 'status': 'CHANGE', 'value1_old': '', 'value2_new': 'so much'}
            ]},
            {'key': 'key', 'status': 'STAY', 'value': 'value'},
            {'key': 'ops', 'status': 'ADD', 'value': 'vops'}
        ]}
    ]},
    {'key': 'group1', 'status': 'NESTED', 'value': [
        {'key': 'baz', 'status': 'CHANGE', 'value1_old': 'bas', 'value2_new': 'bars'},
        {'key': 'foo', 'status': 'STAY', 'value': 'bar'},
        {'key': 'nest', 'status': 'CHANGE', 'value1_old': {'key': 'value'}, 'value2_new': 'str'}
    ]},
    {'key': 'group2', 'status': 'DEL', 'value': {'abc': 12345, 'deep': {'id': 45}}},
    {'key': 'group3', 'status': 'ADD', 'value': {'deep': {'id': {'number': 45}},
                                                 'fee': 100500}}
]



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
    if status != 'CHANGE':
        if status == 'NESTED':
            return '\n'.join(list(map(lambda x: build_plain_tree(
                x, key + '.'), dict_['value'])))
        if status == 'ADD':
            value = get_value(dict_['value'])
            return get_head(key) + f'added with value: {value}'
        if status == 'DEL':
            return get_head(key) + 'removed'
        return ''
    value_old = get_value(dict_['value1_old'])
    value_new = get_value(dict_['value2_new'])
    return get_head(key) + f'updated. From {value_old} to {value_new}'


def get_plain_diff(node):
    list_ = []
    for _ in node:
        list_.append(build_plain_tree(_, ''))
    return '\n'.join(list_).replace('\n\n', '\n')


if __name__ == '__main__':
    print(get_plain_diff(diff34))
