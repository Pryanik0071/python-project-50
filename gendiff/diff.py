def get_diff_tree(keys, obj1, obj2):
    list_ = []
    for key in keys:
        if key in obj1 and key in obj2:
            if all((isinstance(obj1.get(key), dict),
                    isinstance(obj2.get(key), dict))):
                new_keys = sorted(
                    set(list(obj1[key].keys()) + list(obj2[key].keys()))
                )
                result = get_diff_tree(new_keys, obj1[key], obj2[key])
                list_.append({
                    "key": key,
                    "status": 'NESTED',
                    "value": result
                })
            else:
                if obj1.get(key) == obj2.get(key):
                    list_.append({
                        "key": key,
                        "status": 'STAY',
                        "value": obj1[key]
                    })
                else:
                    list_.append({
                        "key": key,
                        "status": 'CHANGE',
                        "value1_old": obj1[key],
                        "value2_new": obj2[key]
                    })
        elif key not in obj1:
            list_.append({
                "key": key,
                "status": 'ADD',
                "value": obj2[key]
            })
        else:
            list_.append({
                "key": key,
                "status": 'DEL',
                "value": obj1[key]
            })
    return list_


def get_first_keys(file1, file2):
    list_ = []
    if isinstance(file1, dict):
        list_.extend(list(file1.keys()))
    if isinstance(file2, dict):
        list_.extend(list(file2.keys()))
    return sorted(set(list_))
