import sys
from argparse import ArgumentParser, FileType


def escape_1(char):
    code = ord(char)
    if code > 127:
        return rf"\U{hex(code)[2:]:0>8}"

    return char


# with inline if statement
def escape_2(char):
    code = ord(char)
    return (
        rf"\U{hex(code)[2:]:0>8}"
        if code > 127
        else char 
    )


# Bonus 1 - support chars that can be represented by 4 hexidecimal digits or 
# fewer by using small u
# Bonus 3 - support html "style"
def escape(char, style='default'):
    code = ord(char)
    if code <= 0b0111_1111:
        return char 
    elif style == "html":
        return f"&#{hex(code)[1:]};"
    elif code <= 0xffff:
        return rf"\u{hex(code)[2:]:0>4}"
    else:
        return rf"\U{hex(code)[2:]:0>8}"


def escape_file_1(text_file):
    contents = text_file.read()
    escaped = ""
    for char in contents:
        escaped += escape(char)

    return escaped


def escape_file(text_file, style='default'):
    contents = text_file.read()
    return ''.join(
        escape(c, style)
        for c in contents
    )


# Bonus 2 - support stdin 
''' Original solution supporting stdin
if __name__ == "__main__":
    [filename] = sys.argv[1:]
    if filename == '-':
        print(escape_file(sys.stdin), end='')
    else:
        with open(filename, mode='rt', encoding='utf8') as text_file:
            print(escape_file(text_file), end='')
'''


# Bonus 2 - support stdin with argparse
def main():
    parser = ArgumentParser()
    parser.add_argument('file', type=FileType('rt'))
    parser.add_argument(
        '--style',
        choices=['default', 'html'],
        default='default',
    )
    args = parser.parse_args()
    print(escape_file(args.file, style=args.style), end='')


if __name__ == "__main__":
    main()
