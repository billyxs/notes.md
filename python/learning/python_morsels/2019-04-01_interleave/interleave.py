# https://www.pythonmorsels.com/exercises/d2b9aaca98d845ccaf9905825955e473/

# Articles
# https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
# https://docs.python.org/3/library/itertools.html#itertools.chain.from_iterable


from itertools import chain

# Nailed this solution!
def interleave_(iterable1, iterable2):
    for value1, value2 in zip(iterable1, iterable2):
        yield value1
        yield value2


# Solutions

def interleave_1(sequence1, sequence2):
    """Return 1 item at a time from each list"""
    interleaved = []

    # Whenever you see range(len(...)) use enumerate()
    # for i in range(len(sequence1)):
    for i, _ in enumerate(sequence1):
        interleaved.append(sequence1[i])
        interleaved.append(sequence2[i])
    return interleaved


# Bonus - accept any iterable

def interleave_2(sequence1, sequence2):
    """Return 1 item at a time from each list"""
    interleaved = []
    for item1, item2 in zip(sequence1, sequence2):
        interleaved.append(item1)
        interleaved.append(item2)
    return interleaved


# Bonus - return an iterable 

def interleave_3(sequence1, sequence2):
    """Return 1 item at a time from each list"""
    return (
        item
        for item1, item2 in zip(sequence1, sequence2)
        for item in [item1, item2]
    )


def interleave_4(iterable1, iterable2):
    """Return 1 item at a time from each list"""
    return chain.from_iterable(zip(iterable1, iterable2)) 


def interleave(iterable1, iterable2):
    for item1, item2 in zip(iterable1, iterable2):
        yield item1
        yield item2
