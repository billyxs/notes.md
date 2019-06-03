# https://www.pythonmorsels.com/exercises/83ed2a27b86b41a185036b262fb67c41/
# https://www.pythonmorsels.com/exercises/83ed2a27b86b41a185036b262fb67c41/solution/

from collections import deque


def tail_(sequence, count):
    "my solution - return the last items of a sequence based on a given count"
    if not sequence or  len(sequence) == 0 or count < 1: 
        return []

    seqlist = list(sequence)
    icount = len(seqlist)
    if count >= icount:
        return seqlist

    result = []
    for i, item in enumerate(sequence):
        if (i > icount - count - 1):
            result.append(seqlist[i])
    return result


# Solutions


def tail_1(sequence, count):
    """Return the last n items in a given sequence."""
    if count <= 0:
        return []
    return list(sequence[-count:])


def tail_2(sequence, count):
    """Return the last n items in a given sequence."""
    items = []
    if count <= 0:
        return []
    elif count <= 1:
        index = slice(0, 0)
    else:
        index = slice(-(count - 1), None)
    for item in sequence:
        items = [*items[index], item]
    return items


def tail(sequence, count):
    """Return the last n items in a given sequence."""
    if count <= 0:
        return []
    return list(deque(sequence, maxlen=count))
