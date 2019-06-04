# https://www.pythonmorsels.com/exercises/b8edf79165344da29933573d9f2813a7/


def multimax__(iterable, key=max):
    """first solution - didn't pass last test"""
    if iterable:
        maxnum = key(*iterable)
        return [maxnum] * iterable.count(maxnum)
    return []


def multimax___(iterable, key=lambda x: x):
    """first solution - didn't pass last test"""
    if iterable:
        maxnum = None
        result = []

        for item in iterable:
            if maxnum is None or key(item) > key(maxnum):
                result.clear()
                maxnum = item
            if key(item) >= key(maxnum):
                result.append(item)
        return result
    return []
           

# Solutions


def multimax_1(iterable):
    """Return list of all maximum values."""
    max_item = max(iterable, default=None)
    return [
        item
        for item in iterable
        if item == max_item
    ]


def multimax_2(iterable):
    """Return list of all maximum values."""
    maximums = []
    for item in iterable:
        if not maximums or maximums[0] == item:
            maximums.append(item)
        elif item > maximums[0]:
            maximums = [item]
    return maximums


def multimax(iterable, key=lambda x: x):
    """Return list of all maximum values."""
    max_key = None
    maximums = []
    for item in iterable:
        k = key(item)
        if k == max_key:
            maximums.append(item)
        elif not maximums or k > max_key:
            maximums = [item]
            max_key = k
    return maximums


