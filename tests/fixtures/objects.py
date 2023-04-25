file1 = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False
}

file2 = {
    'timeout': 20,
    'verbose': True,
    'host': 'hexlet.io'
}

keys12 = ['follow', 'host', 'proxy', 'timeout', 'verbose']
keys10 = ['follow', 'host', 'proxy', 'timeout']
keys02 = ['host', 'timeout', 'verbose']

diff12 = [
    {'key': 'follow', 'status': 'DELETED', 'value': False},
    {'key': 'host', 'status': 'UNCHANGED', 'value': 'hexlet.io'},
    {'key': 'proxy', 'status': 'DELETED', 'value': '123.234.53.22'},
    {'key': 'timeout', 'status': 'CHANGED',
     'value1_old': 50, 'value2_new': 20},
    {'key': 'verbose', 'status': 'ADDED', 'value': True}
]

diff34 = [
    {'key': 'common', 'status': 'NESTED', 'value': [
        {'key': 'follow', 'status': 'ADDED', 'value': False},
        {'key': 'setting1', 'status': 'UNCHANGED', 'value': 'Value 1'},
        {'key': 'setting2', 'status': 'DELETED', 'value': 200},
        {'key': 'setting3', 'status': 'CHANGED',
         'value1_old': True, 'value2_new': None},
        {'key': 'setting4', 'status': 'ADDED', 'value': 'blah blah'},
        {'key': 'setting5', 'status': 'ADDED', 'value': {'key5': 'value5'}},
        {'key': 'setting6', 'status': 'NESTED', 'value': [
            {'key': 'doge', 'status': 'NESTED', 'value': [
                {'key': 'wow', 'status': 'CHANGED',
                 'value1_old': '', 'value2_new': 'so much'}
            ]},
            {'key': 'key', 'status': 'UNCHANGED', 'value': 'value'},
            {'key': 'ops', 'status': 'ADDED', 'value': 'vops'}
        ]}
    ]},
    {'key': 'group1', 'status': 'NESTED', 'value': [
        {'key': 'baz', 'status': 'CHANGED',
         'value1_old': 'bas', 'value2_new': 'bars'},
        {'key': 'foo', 'status': 'UNCHANGED', 'value': 'bar'},
        {'key': 'nest', 'status': 'CHANGED',
         'value1_old': {'key': 'value'}, 'value2_new': 'str'}
    ]},
    {'key': 'group2', 'status': 'DELETED',
     'value': {'abc': 12345, 'deep': {'id': 45}}},
    {'key': 'group3', 'status': 'ADDED',
     'value': {'deep': {'id': {'number': 45}},
               'fee': 100500}}
]
