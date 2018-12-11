# https://www.pythonmorsels.com/exercises/9af6665915964ee7ba19fe3d762d9ca8/

from string import punctuation


def count_words(str):
    "my solution - count words in a sentence"
    w = str.lower().split()
    b = {}
    for v in w:
        value = v.strip(punctuation + '¿')
        if value in b:
            b[value] += 1
        else:
            b[value] = 1

    return b
