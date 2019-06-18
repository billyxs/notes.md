# https://www.pythonmorsels.com/exercises/850c1b8fce804b3ea99fffe26273051d/
# https://www.pythonmorsels.com/exercises/850c1b8fce804b3ea99fffe26273051d/solution/

from csv import DictReader
import csv
from collections import defaultdict, OrderedDict 
from itertools import zip_longest


def csv_columns_(csv_file, *, headers=None, missing=None):
    """Take a csv file and group data with headers"""
    rows = ["".join(row.strip()) for row in csv_file]
    header_list = headers or rows[0].split(',')
    result = defaultdict(list)

    if headers is None:
        rows = rows[1:]

    for idx, item in enumerate(rows):
        print('item = ', item)
        for i, value in enumerate(item.split(',')):
            header = header_list[i]
            result[header].append(value)

    return result 


# Solutions

def csv_columns_1(csv_file, *, headers=None, missing=None):
    """Return dictionary mapping headers to corresponding columns"""
    reader = csv.reader(csv_file)
    columns = {}
    for row in reader:
        if headers is None:
            headers = row
            columns = {
                header: []
                for header in headers
            }
            continue
        for header, item in zip(headers, row):
            columns.setdefault(header, []).append(item)
    return columns


def csv_columns_2(csv_file, headers=None, missing=None):
    """Return dictionary mapping headers to corresponding columns"""
    reader = csv.reader(csv_file)
    headers = next(reader)
    return {
        header: column
        for header, *column in zip(headers, *reader)
    }


def csv_columns_3(csv_file, headers=None, missing=None):
    """Return dictionary mapping headers to corresponding columns"""
    columns = defaultdict(list)
    reader = DictReader(csv_file)
    for row in reader:
        for name, value in row.items():
            columns[name].append(value)
    
    return columns


def csv_columns_4(csv_file, headers=None, missing=None):
    """Return dictionary mapping headers to corresponding columns"""
    reader = csv.reader(csv_file)
    headers = next(reader)
    return OrderedDict([
        (header, column)
        for header, *column in zip(headers, *reader)
    ])


def csv_columns_5(csv_file, *, headers=None, missing=None):
    """Return dictionary mapping headers to corresponding columns"""
    reader = csv.reader(csv_file)
    if not headers:
        headers = next(reader)

    columns = {header: [] for header in headers}
    for row in reader:
        for i, header in enumerate(headers):
            try:
                columns[header].append(row[i])
            except IndexError:
                columns[header].append(missing)

    return columns
                

def csv_columns_6(csv_file, *, headers=None, missing=None):
    """Return dictionary mapping headers to corresponding columns"""
    reader = csv.reader(csv_file)
    if headers is None:
        headers = next(reader)

    columns = zip_longest(*reader, fillvalue=missing)
    return {
        header: list(column)
        for header, column in zip(headers, columns)
    }


def csv_columns(csv_file, *, headers=None, missing=None):
    """Return dictionary mapping headers to corresponding columns"""
    columns = defaultdict(list)
    reader = DictReader(csv_file, fieldnames=headers, restval=missing)
    for row in reader:
        for name, value in row.items():
            columns[name].append(value)
    return columns
