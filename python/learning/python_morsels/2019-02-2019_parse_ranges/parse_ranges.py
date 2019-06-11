# https://www.pythonmorsels.com/exercises/008c3f7419944ed781eb4924483bff35/

import re


def parse_ranges_(ranges):
    """parse ranges"""

    result = []
    for item in ranges.replace(' ', '').split(','):
        first, last = (item.split('-') + [None])[:2]
        if last is None or first == last:
            result.append(int(first))
        else:
            result.extend(range(int(first), int(last)+1))

    return result 


# Solutions

def parse_ranges_1(ranges):
    numbers = []
    for group in ranges.split(','):
        start, stop = group.split('-')
        for num in range(int(start), int(stop)+1):
            numbers.append(num)
    return numbers

def parse_ranges_2(ranges):
    pairs = []
    for group in ranges.split(','):
        pairs.append(group.split('-'))

    numbers = []
    for start, stop in pairs:
        for num in range(int(start), int(stop)+1):
            numbers.append(num)
    return numbers


def parse_ranges_3(ranges):
    pairs = (
        group.split('-')
        for group in ranges.split(',')
    )

    return (
        num
        for start, stop in pairs
        for num in range(int(start), int(stop)+1)
    )


def parse_ranges_4(ranges):
    pairs = re.findall(r'\b(\d+)-(\d+)\b', ranges)
    return (
        num
        for start, stop in pairs
        for num in range(int(start), int(stop)+1)
    )


PAIRS_RE = re.compile(r'( \d+ ) - ( \d+ )', re.VERBOSE)
def parse_ranges_5(ranges):
    return (
        num
        for start, stop in PAIRS_RE.findall(ranges)
        for num in range(int(start), int(stop)+1)
    )


def parse_ranges_6(ranges):
    pairs = (
        group.split('-') if '-' in group else (group, group)
        for group in ranges.split(',')
    )
    for start, stop in pairs:
        yield from range(int(start), int(stop)+1)


def parse_ranges_7(ranges):
    pairs = (
        group.split('-') if '-' in group else (group, group)
        for group in ranges.split(',')
    )
    for start, stop in pairs:
        yield from range(int(start), int(stop)+1)

# Bonus 3


def partition_1(sep, group):
    a, _, b = group.partition(sep)
    return ((a, b) if b and not b.startswith('>') else (a, a))

def parse_ranges_8(ranges):
    pairs = (
        partition_1('-', group)
        for group in ranges.split(',')
    )
    return (
        num
        for start, stop in pairs
        for num in range(int(start), int(stop)+1)
    )


def parse_ranges_9(ranges):
    for group in ranges.split(','):
        start, sep, end = group.partition('-')
        if end.startswith('>') or not sep:
            yield int(start)
        else:
            yield from range(int(start), int(end)+1)


def partition_2(sep, group):
    """Return (start, end) tuple from given number group."""
    group = re.sub(r'->.*', r'', group)
    a, _, b = group.partition(sep)
    return ((a, b) if b else (a, a))


def parse_ranges(ranges):
    pairs = (
       partition_2('-', group) 
       for group in ranges.split(',')
    )
    return (
        num
        for start, stop in pairs
        for num in range(int(start), int(stop)+1)
    )
