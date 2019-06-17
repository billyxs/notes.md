# https://www.pythonmorsels.com/exercises/03a551781d7548539d42897e5e8a1519/
from math import ceil
from itertools import count, takewhile


def float_range_(start, end=None, step=1.0):
    if end is None:
        start = 0.0
        end = start

    result = []
    while start < end:
        result.append(float(start) )
        start = end + step

    return result


# Solutions

def float_range_1(start, stop=None, step=1):
    """Return iterable numbers from start to stop by step"""
    if stop is None:
        start, stop = 0, start
    i = start
    if step > 0:
        while i < stop:
            yield i
            i += step
    else:
        while i > stop:
            yield i
            i += step


def float_range_2(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    item_count = ceil((stop-start) / step)
    return (
        start+i*step
        for i in range(item_count)
    )


def float_range_3(start, stop=None, step=1):
    if stop is None:
        start, stop = 0 , start

    numbers = (
        start+i*step
        for i in count()
    )
    if step > 0:
        return takewhile(lambda n : n < stop, numbers)
    else:
        return takewhile(lambda n : n > stop, numbers)



class float_range:

    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        (self.start, self.stop, self.step) = (start, stop, step)

    @staticmethod
    def _attrs(self):
        if len(self) == 0:
            return ()
        step = 1 if len(self) else self.step
        return (next(iter(self)), next(reversed(self)), step)

    def __eq__(self, other):
        if isinstance(other, (float_range, range)):
            return self._attrs(self) == self._attrs(other)
        else:
            return NotImplemented

    def __len__(self):
        return max(ceil((self.stop-self.start) / self.step), 0)

    def __iter__(self):
        i = self.start
        for _ in range(len(self)):
            yield i
            i += self.step

    def __reversed__(self):
        i = self.start + (len(self)-1)*self.step
        for _ in range(len(self)):
            yield i
            i -= self.step
