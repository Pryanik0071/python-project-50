from gendiff import check_values, get_diff


def test_check_values_one():
    key = 'Test'
    value1 = 123
    value2 = 123
    assert check_values(key, value1, value2) == {
        f'  {key}': value1,
    }


def test_check_values_two():
    key = 'Test'
    value1 = 123
    value2 = 234
    assert check_values(key, value1, value2) == {
        f'- {key}': value1,
        f'+ {key}': value2
    }


def test_check_values_three():
    key = 'Test'
    value1 = 123
    value2 = None
    assert check_values(key, value1, value2) == {
        f'- {key}': value1
    }


def test_check_values_four():
    key = 'Test'
    value1 = None
    value2 = 123
    assert check_values(key, value1, value2) == {
        f'+ {key}': value2
    }


def test_get_diff():
    symbol = '-'
    key = 'str_'
    value = 123
    assert get_diff(key, value, symbol) == {
        f'{symbol} {key}': value
    }


def test_get_diff_default():
    key = 'str_'
    value = 123
    assert get_diff(key, value) == {
        f'  {key}': value
    }
