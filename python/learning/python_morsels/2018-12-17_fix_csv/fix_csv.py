import csv
import sys

delimiter = "|"
quote = "'"
original_filename = None
result_filename = None

def getArgValue(arg):
    return arg.split('=')[1]


for item in sys.argv:
    print(item)
    if item.startswith('--in-delimiter'):
        delimiter = getArgValue(item)
    if item.startswith('--in-quote'):
        quote = getArgValue(item)
    if original_filename is not None and item.find('.csv') > 0:
        result_filename = item
    if original_filename is None and item.find('.csv') > 0:
        original_filename = item

print(original_filename, result_filename)

with open(original_filename, mode='r') as infile:
    reader = csv.reader(infile, delimiter=delimiter, quotechar=quote)
    with open(result_filename, mode='w') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(reader)
