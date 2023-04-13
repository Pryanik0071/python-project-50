def status(status):
    if status == 'STAY':
        return '    '
    if status == 'ADD':
        return '  + '
    return '  - '


def space(deep):
    return f'{" " * (4 * deep)}'


def check(st):
    if st == '':
        return ''
    if st is False:
        return ' false'
    if st is True:
        return ' true'
    return f' {st}'


def value(val, deep):
    list_ = []
    if isinstance(val, dict):
        if len(val) == 1:
            key, value_ = list(val.items())[0]
            return ' {\n' + f'{space(deep + 1)}{key}:{value(value_, deep + 1)}' + f'\n{space(deep)}' + '}'
        else:
            for key, values in val.items():
                list_.append(f'\n{space(deep + 1)}{key}:{value(values, deep + 1)}')
            return ' {' + ''.join(list_) + f'\n{space(deep)}' + '}'
    return check(val)


def t(dict_, deep):
    if dict_.get('status') in ('STAY', 'ADD', 'DEL'):
        if isinstance(dict_['value'], list):
            result = '\n'.join(list(map(lambda x: t(x, deep + 1), dict_['value'])))
            return f'{space(deep)}{status(dict_["status"])}{dict_["key"]}:' + ' {\n' + f'{result}' + f'\n{space(deep + 1)}' + '}'
        return f'{space(deep)}{status(dict_["status"])}{dict_["key"]}:' + f'{value(dict_["value"], deep + 1)}'
    result1 = dict_['value1_old']
    result2 = dict_['value2_new']
    r1_ = f'{value(result1, deep + 1)}'
    r2_ = f'{value(result2, deep + 1)}'
    return f'{space(deep)}{status("")}{dict_["key"]}:{r1_}' \
           f'\n{space(deep)}{status("ADD")}{dict_["key"]}:{r2_}'


def get_stylish_diff(node):
    l_ = []
    for i in node:
        l_.append(t(i, 0))
    return '{\n' + '\n'.join(l_) + '\n}'