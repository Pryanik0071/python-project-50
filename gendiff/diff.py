def get_diff_tree(obj1, obj2):
    tree = []
    keys = sorted(obj1.keys() | obj2.keys())
    for key in keys:
        if all((isinstance(obj1.get(key), dict),
                isinstance(obj2.get(key), dict))):
            result = get_diff_tree(obj1[key], obj2[key])
            tree.append({
                'key': key,
                'status': 'NESTED',
                'value': result
            })
        elif key not in obj1:
            tree.append({
                'key': key,
                'status': 'ADDED',
                'value': obj2[key]
            })
        elif key not in obj2:
            tree.append({
                'key': key,
                'status': 'DELETED',
                'value': obj1[key]
            })
        elif obj1.get(key) == obj2.get(key):
            tree.append({
                'key': key,
                'status': 'UNCHANGED',
                'value': obj1[key]
            })
        else:
            tree.append({
                'key': key,
                'status': 'CHANGED',
                'value_old': obj1[key],
                'value_new': obj2[key]
            })
    return tree
