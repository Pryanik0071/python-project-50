from gendiff import check_values


def test_one():
    key = 'Test'
    value1 = 123
    value2 = 123
    assert check_values(key, value1, value2) == {
        key: value1,
    }
