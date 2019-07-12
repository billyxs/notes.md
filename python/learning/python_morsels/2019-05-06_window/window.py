# https://www.pythonmorsels.com/exercises/4c2a9fe5bcbb49e69f2fabb03a178bee/

from collections import deque 
from itertools import islice


def window_(iterable, length):
    """Returns a list of tuples of items in given list and next n-1 items."""
    return (
        tuple(iterable[idx:(idx+length)])
        for idx, item in enumerate(iterable)
        if idx + length <= len(iterable) 
    )


# Solutions

def window_1(sequence, n):
    """Returns a list of tuples of items in given list and next n-1 items."""
    items = []
    for i in range(len(sequence)):
        if i+n <= len(sequence):
            items.append(tuple(sequence[i:i+n]))

def window_2(sequence, n):
    """Returns a list of tuples of items in given list and next n-1 items."""
    sequences = [sequence[i:] for i in range(n)]
    return zip(*sequences)

# Bonus 1 - accept any iterable

def window_3(iterable, n):
    """Returns a list of tuples of items in given list and next n-1 items."""
    items = []
    current = ()
    for item in iterable:
        if len(current) < n:
            current = current + (item,)
        else:
            current = current[1:] + (item,)
        if len(current) == n:
            items.append(current)
    return items

# with tuple unpacking

def window_4(iterable, n):
    """Returns a list of tuples of items in given list and next n-1 items."""
    items = []
    current = ()
    for item in iterable:
        if len(current) < n:
            current = (*current, item,)
        else:
            current = (*current[1:], item)
        if len(current) == n:
            items.append(current)
    return items


# Bonus 2 - return an iterator

def window_5(iterable, n): 
    """Yield tuples including iterable item and the next n-1 items."""
    current = ()
    for item in iterable:
        current = (*current[max(len(current)-n+1, 0):], item)
        if len(current) == n:
            yield current


def window(iterable, n): 
    """Yield tuples including iterable item and the next n-1 items."""
    iterator = iter(iterable)
    current = deque(islice(iterator, n), maxlen=n)
    yield tuple(current)
    for item in iterator:
        current.append(item)
        yield tuple(current)

