# https://www.pythonmorsels.com/exercises/02e33401dd3b427d8d379311eac666ac/
# https://www.pythonmorsels.com/exercises/02e33401dd3b427d8d379311eac666ac/solution/

from itertools import groupby


def compact(l):
    """remove adjacent duplicates and return an iterable"""
    print(type(l))
    if l:
        result = [] 
        lastitem = 'xxxx'
        for i in iter(l):
            if lastitem != i:
                lastitem = i
                result.append(i)

        return iter(result)
        
    return l


# Solutions


def compact_1(seq):
    """Return new iterable with adjacent duplicate values removed."""
    deduped = []
    for i, item in enumerate(seq):
        if i == 0 or item != seq[i-1]:
            deduped.append(item)

    return deduped


def compact_2(seq):
    """Return new iterable with adjacent duplicate values removed."""
    deduped = []
    for item, previous in zip(seq, [object(), *seq]):
        if item != previous:
            deduped.append(item)

    return deduped


def compact_3(seq):
    """Return new iterable with adjacent duplicate values removed."""
    deduped = []
    previous = object()
    for item in seq:
        if item != previous:
            deduped.append(item)
            previous = item
    return deduped

    
def compact_4(seq):
    return (
        item
        for item, group in groupby(seq)
    )

