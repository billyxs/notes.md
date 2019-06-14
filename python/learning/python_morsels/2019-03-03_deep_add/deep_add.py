# https://www.pythonmorsels.com/exercises/212c00f2c19846e5b9ac365aa5cf4026/

from collections.abc import Iterable
from numbers import Number


def deep_add_(iterable, start=0):
    for item in iterable:
        if isinstance(item, iterable):
            start += deep_add(item)
        else:
            start += item
    return start


# Solutions

def deep_add_1(lists):
    """Return sum of values in given list, iterating deeply."""
    total = 0
    lists = list(lists)
    while lists:
        item = lists.pop()
        if isinstance(item, list):
            lists.extend(item)
        else:
            total += item
    return total


def deep_add_2(list_or_number):
    """Return sum of values in given list, iterating deeply."""
    if type(list_or_number) == list:
        return sum(deep_add(x) for x in list_or_number)
    else:
        return list_or_number


def deep_add_3(list_or_number):
    """Return sum of values in given list, iterating deeply."""
    return (
        sum(deep_add(x) for x in list_or_number)
        if type(list_or_number) == list
        else list_or_number
    )


def deep_add_4(iterable_or_number):
    """Return sum of values in given list, iterating deeply."""
    if isinstance(iterable_or_number, Number):
        return iterable_or_number

    return sum(deep_add(x) for x in iterable_or_number)


def deep_add_5(iterable_or_number, start=0):
    """Return sum of values in given iterable, iterating deeply."""
    if isinstance(iterable_or_number, Number):
        return iterable_or_number
    else:
        total = start
        for x in iterable_or_number:
            total += deep_add(x)
        return total


def deep_add_6(iterable_or_number, start=0):
    """Return sum of values in given iterable, iterating deeply."""
    if isinstance(iterable_or_number, Number):
        return iterable_or_number
    else:
        return sum((deep_add(x) for x in iterable_or_number), start)


def deep_add_7(iterable_or_number, start=0):
    """Return sum of values in given iterable, iterating deeply"""
    try:
        iter(iterable_or_number)
    except TypeError:
        return iterable_or_number
    else:
        return sum((deep_add(x) for x in iterable_or_number), start)


def deep_add_8(iterable_or_number, start=0):
    """Return sum of values in given iterable, iterating deeply"""
    if hasattr(iterable_or_number, '__iter__'):
        return sum((deep_add(x) for x in iterable_or_number), start)
    else:
        return iterable_or_number


def deep_add(iterable_or_number, start=0):
    """Return sum of values in given iterable, iterating deeply."""
    if isinstance(iterable_or_number, Iterable):
        return sum((deep_add(x) for x in iterable_or_number), start)
    else:
        return iterable_or_number
