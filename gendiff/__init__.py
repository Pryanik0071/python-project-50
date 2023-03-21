import json

__all__ = (
    'generate_diff',
)


def get_diff(key, value, symbol: str = ' ') -> dict:
    return {f'{symbol} {key}': value}


def generate_diff(file_path1, file_path2):
    json1 = json.load(open(file_path1))
    json2 = json.load(open(file_path2))
    keys = sorted(set(list(json1.keys()) + list(json2.keys())))
    dict_ = {}
    for key in keys:
        dict_.update(check_values(key, json1.get(key), json2.get(key)))
    return json.dumps(dict_, indent=4).replace('\"', '')


def check_values(key, value1, value2):
    if value1 and value2:
        if value1 != value2:
            dict_ = {}
            dict_.update(get_diff(key, value1, '-'))
            dict_.update(get_diff(key, value2, '+'))
            return dict_
        return get_diff(key, value1)
    if value1 is not None:
        return get_diff(key, value1, '-')
    return get_diff(key, value2, '+')
