# https://www.pythonmorsels.com/exercises/c761e15e7ba84d63a18c79929e2dfccf/

from datetime import timedelta
import math
import re


def normalize_timestamp(timestamp):
    items = timestamp.split(':')
    if len(items) is 2:
        items.insert(0, '00')

    return items

def sum_timestamps_(timestamps):
    total = 0
    for timestamp in timestamps:
        hours, minutes, seconds = normalize_timestamp(timestamp) 
        total += int(seconds)
        total += 60 * int(minutes)
        total += 60 * 60 * int(hours)

    hour = math.floor(total / 3600)
    minute = math.floor((total - (hour * 3600)) / 60)
    second = total - (hour * 3600) - (minute * 60)

    if hour > 0 and minute < 10:
        minute = '0' + str(minute)

    if second < 10:
        second = '0' + str(second)

    endtime = [str(minute), str(second)]

    if hour > 0:
        endtime.insert(0, str(hour))

    return ":".join(endtime)


# Solutions

def sum_timestamps_1(timestamps):
    total_time = 0
    for time in timestamps:
        minutes, seconds = time.split(':')
        total_time += int(minutes) * 60 + int(seconds)

    minutes = total_time // 60
    seconds = total_time % 60
    if seconds < 10:
        return f"{minutes}:0{seconds}"
    else:
        return f"{minutes}:{seconds}"

# Shorten the 2 digit requirement
def sum_timestamps_2(timestamps):
    total_time = 0
    for time in timestamps:
        minutes, seconds = time.split(':')
        total_time += int(minutes) * 60 + int(seconds)

    minutes, seconds = divmod(total_time, 60)
    return f"{minutes:01d}:{seconds:02d}"

# divide up responsibilities
def parse_time_1(time_string):
    minutes, seconds = time_string.split(':')
    return int(minutes) * 60 + int(seconds)

def format_time_1(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:01d}:{seconds:02d}"

def sum_timestamps_3(timestamps):
    total_time = 0
    for time in timestamps:
        total_time += parse_time_1(time)

    return format_time_1(total_time)


# move main function to use a generator
def sum_timestamps_4(timestamps):
    return format_time_1(sum(
        parse_time_1(time)
        for time in timestamps
    ))


# make it more readable as a one liner
def sum_timestamps_5(timestamps):
    return format_time_1(sum(parse_time_1(t) for t in timestamps))


# use timedelta objects - above is preferred but this is different
def parse_time_2(time_string):
    minutes, seconds = time_string.split(':')
    return timedelta(minutes=int(minutes), seconds=int(seconds))

def format_time_2(delta):
    minutes, seconds = divmod(delta.seconds, 60)
    return f"{minutes:01d}:{seconds:02d}"

def sum_timestamps_6(timestamps):
    deltas = (parse_time_2(t) for t in timestamps)
    total_time = sum(deltas, timedelta(0))
    return format_time_2(total_time)

# remove need for format_time 
def sum_timestamps_7(timestamps):
    deltas = (parse_time_2(t) for t in timestamps)
    total_time = sum(deltas, timedelta(0))
    time = str(total_time)[2:]
    return time[1:] if time.startswith('0') else time


# Bonus 1 - return timestmap to include hours when necessary

# update format_time with another divmod for hours and output with hours when appropriate
def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    else:

        return f"{minutes:01d}:{seconds:02d}"


# Bonus 2 - 

def parse_time_3(time_string):
    sections = time_string.split(':')
    try:
        hours, minutes, seconds = sections
    except ValueError:
        hours = 0
        minutes, seconds = sections
        return int(hours) * 3600 + int(minutes)*60 + int(seconds)


# use list comprehension instead of try/except
def parse_time_4(time_string):
    sections = [int(s) for s in time_string.split(':')]
    if len(sections) > 2:
        hours, minutes, seconds = sections
    else:
        hours, (minutes, seconds) = 0, sections
    return hours*3600 + minutes*60 + seconds


# using regex for parse time
TIME_RE = re.compile(r'''
    ^
    (?:
        ( \d + )
        :
    )?
    ( \d + )
    :
    ( \d + )
    $
''', re.VERBOSE)

def parse_time(time_string):
    hours, minutes, seconds = TIME_RE.search(time_string).groups()
    return int(hours or 0)*3600 + int(minutes)*60 + int(seconds)


# parse time with name regex groups
TIME_RE_NAMED = re.compile(r'''
    ^
    (?:
        (?P<hours> \d + )
        :
    )?
    (?P<minutes> \d + )
    :
    (?P<seconds> \d + )
    $
''', re.VERBOSE)

def parse_time_named(time_string):
    match = TIME_RE_NAMED.search(time_string)
    return (
        int(match.group('seconds')) +
        int(match.group('minutes')) * 60 +
        int(match.group('hours') or 0) * 3600
    )


# copied from above for other solutions
def sum_timestamps(timestamps):
    return format_time(sum(parse_time(t) for t in timestamps))
