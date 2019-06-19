# https://www.pythonmorsels.com/exercises/66154fc44ddb4382b7964f60a7446bfa/

from itertools import dropwhile

def lstrip_(iterable, remove):
    found = None
    def removeIt(x):
        return x == remove

    removeFunc = removeIt 
    if callable(remove):
        removeFunc = remove

    for item in iterable:
        if found is None and not removeFunc(item):
            found = True
        if found is not None:
            yield item


# Solutions

def lstrip_1(iterable, strip_value):
    """Return iterable with items removed from beginning"""
    stripped = []
    is_beginning = True
    for item in iterable:
        if is_beginning and item == strip_value:
            continue
        is_beginning = False
        stripped.append(item)
    return stripped


def lstrip_2(iterable, strip_value):
    """Return iterable with items removed from beginning"""
    stripped = []
    iterator = iter(iterable)
    for item in iterator:
        if not item == strip_value:
            stripped.append(item)
            break
    for item in iterator:
        stripped.append(item)
    return stripped


def lstrip_3(iterable, strip_value):
    """Return iterable with items removed from beginning"""
    def is_strip_value(value): return value == strip_value
    return dropwhile(is_strip_value, iterable) 

# Bonus 1 - return an iterator


def lstrip_4(iterable, strip_value):
    """Return iterable with items removed from beginning"""
    iterator= iter(iterable)
    for item in iterator:
        if item != strip_value:
            yield item
            break
    for item in iterator:
        yield item
    

# Using yield from for python 3
def lstrip_5(iterable, strip_value):
    """Return iterable with items removed from beginning"""
    iterator= iter(iterable)
    for item in iterator:
        if item != strip_value:
            yield item
            break
    yield from iterator
    

# Bonus 2 - accept a function for the strip value check
def lstrip_6(iterable, strip_value):
    """Return iterable with items removed from beginning"""
    iterator = iter(iterable)
    for item in iterator:
        # complex if statement
        if (callable(strip_value) and not strip_value(item) or not callable(strip_value) and item != strip_value):
            yield item
            break
    yield from iterator


def lstrip_7(iterable, strip_value):
    """Return iterable with items removed from beginning"""
    iterator = iter(iterable)
    if callable(strip_value):
        predicate = strip_value
    else:
        def predicate(value): return value == strip_value
    for item in iterator:
        if not predicate(item):
            yield item
            break
    yield from iterator


def lstrip(iterable, strip_value):
    """Return iterable with items removed from beginning"""
    if callable(strip_value):
        predicate = strip_value
    else:
        def predicate(value): return value == strip_value
    return dropwhile(predicate, iterable)
