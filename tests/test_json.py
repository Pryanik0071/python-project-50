from gendiff import check_values


def test_one():
    key = 'Test'
    value1 = 123
    value2 = 123
    assert check_values(key, value1, value2) == {
        f'  {key}': value1,
    }


def test_two():
    key = 'Test'
    value1 = 123
    value2 = 234
    assert check_values(key, value1, value2) == {
        f'- {key}': value1,
        f'+ {key}': value2
    }