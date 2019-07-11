# https://www.pythonmorsels.com/exercises/60e1acc807664feb8597712ac6a314f5/

# Added reading
# Facts and myths about Python names and values - https://nedbatchelder.com/text/names.html
# Regular expressions - http://pycon2017.regex.training/

import re

import datetime
from dateutil.parser import parse

def entries_by_date_(entries):
    parsed_entries = []
    for item in entries:
        item = item.strip()
        if item:
            try:
                if parse(item):
                    parsed_entries.append((item,))
            except ValueError:
                parsed_entries[-1] = parsed_entries[-1] + (item,)

    return parsed_entries 


# Solutions

def entries_by_date_1(diary_file):
    entries_by_date = []
    for line in diary_file:
        if line.startswith('201'):
            entries_by_date.append((line.rstrip(), ""))
        else:
            date, entry = entries_by_date[-1]
            entries_by_date[-1] = (date, f"{entry}{line}")

    return [
        (date, entry.strip())
        for (date, entry) in entries_by_date
    ] 


def entries_by_date_2(diary_file):
    entries_by_date = []
    for line in diary_file:
        if line.startswith('201'):
            entry = []
            entries_by_date.append((line.rstrip(), entry))
        else:
            entry.append(line.rstrip())

    return [
        (date, "\n".join(entry).strip())
        for (date, entry) in entries_by_date
    ] 


def entries_by_date_3(diary_file):
    date, entry = None, ""
    for line in diary_file:
        if line.startswith('201'):
            if date:
                yield date, entry.strip()
            date, entry = line.rstrip(), ""
        else:
            entry += line

    yield date, entry.strip()


DATE_RE = re.compile(r'^ \d{4} - \d{2} - \d{2} $', re.VERBOSE)
def entries_by_date_4(diary_file):
    date = None
    for line in diary_file:
        if DATE_RE.search(line):
            if date:
                yield date, entry.strip()
            date, entry = line.rstrip(), ""
        else:
            entry += line

    yield date, entry.strip()


def entries_by_date_5(diary_file):
    return re.findall(r'''
      ( \d{4} - \d{2} - \d{2} )
      [\n] [\n]
      ( .+? )
      (?= \n \n \d{4} - \d{2} - \d{2} | $ )
    ''', diary_file.read(), re.VERBOSE | re.DOTALL)


REPLACEMENTS = {
    (" ", " "),
    ("&nbsp;", " "),
    ("&quot;", '"'),
    ("&", '&'),
    ("&amp;", '&'),
}
def clean_entry(text):
    for original, replacement in REPLACEMENTS:
        text = text.replace(original, replacement)
    return text.strip()



def entries_by_date(diary_file):
    date = None
    for line in diary_file:
        if DATE_RE.search(line):
            if date:
                yield date, clean_entry(entry)
            date, entry = line.rstrip(), ""
        else:
            entry += line
    yield date, clean_entry(entry)
