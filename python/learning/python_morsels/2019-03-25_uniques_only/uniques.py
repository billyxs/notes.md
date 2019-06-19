# https://www.pythonmorsels.com/exercises/b684cd595ca745398131f2252ca13064/

from collections.abc import Hashable


def uniques_only_(iterable):
    """Return uniques of list"""
    track = []
    for i in iterable:
        if i not in track:
            track.append(i)
            yield i


# Solutions

def uniques_only_1(iterable):
    """Return uniques of list"""
    track = set() 
    result = []
    for i in iterable:
        if i not in track:
            track.add(i)
            result.append(i)
    return result


def uniques_only_2(iterable):
    """Return uniques of list"""
    return dict.fromkeys(iterable).keys()

# Bonus 1


def uniques_only_3(iterable):
    """Return uniques of list"""
    track = set() 
    for i in iterable:
        if i not in track:
            yield i
            track.add(i)

# Bonus 2


def uniques_only_4(iterable):
    """Return uniques of list"""
    track = [] 
    for i in iterable:
        if i not in track:
            yield i
            track.append(i)

# Bonus 3


def uniques_only_5(iterable):
    seen_hashable = set()
    seen_unhashable = [] 
    for item in iterable:
        if isinstance(item, Hashable):
            if item not in seen_hashable:
                yield item
                seen_hashable.add(item)
        else:
            if item not in seen_unhashable:
                yield item
                seen_unhashable.append(item)
    

def uniques_only(iterable):
    seen_hashable = set()
    seen_unhashable = [] 
    for item in iterable:
        try:
            if item not in seen_hashable:
                yield item
                seen_hashable.add(item)
        except TypeError:
            if item not in seen_unhashable:
                yield item
                seen_unhashable.append(item)
    
