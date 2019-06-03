# https://www.pythonmorsels.com/exercises/b8520efdf5b3442799f5b4a8a399c32d/
# https://www.pythonmorsels.com/exercises/b8520efdf5b3442799f5b4a8a399c32d/solution/

from collections import defaultdict


def group_by__(sequence, **kwargs):
    """group values based on their derived result"""
    func = kwargs.get('key_func', lambda x : x)

    result = {}
    for item in sequence:
        value = func(item)
        if not result.get(value):
            result[value] = []
        result[value].append(item)
    return result


# Solutions

def group_by_1(iterable, key_func):
    groups = {}
    for item in iterable:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups


def group_by_2(iterable, key_func):
    groups = {}
    for item in iterable:
        key = key_func(item)
        groups.setdefault(key, []).append(item)
    return groups


def group_by_3(iterable, key_func):
    groups = defaultdict(list) 
    for item in iterable:
        groups[key_func(item)].append(item)
    return groups


def group_by(iterable, key_func=lambda x : x):
    groups = defaultdict(list) 
    for item in iterable:
        groups[key_func(item)].append(item)
    return groups
