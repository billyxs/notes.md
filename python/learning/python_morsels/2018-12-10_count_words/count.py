# https://www.pythonmorsels.com/exercises/9af6665915964ee7ba19fe3d762d9ca8/
# https://www.pythonmorsels.com/exercises/9af6665915964ee7ba19fe3d762d9ca8/solution/

from string import punctuation
from collections import defaultdict, Counter
import re


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


def count_words_1(str):
    "review solution with defaultdict - count words in a sentence"
    count = defaultdict()
    for word in str.split():
        count[word] += 1

    return count 


def count_words_2(str):
    "review solution with Counter - count words in a sentence"
    return Counter(str.lower().split()) 


def count_words_3(str):
    "review solution bonus - ignore punctuation - count words in a sentence"
    words = []
    for word in str.lower().split():
        words.append(word.strip(',;.!?")()'))
    return Counter(words) 


def count_words_4(str):
    "review solution ignore punctuation - count words in a sentence"
    return Counter(re.findall(r"[\w'-]+", str.lower()))


def count_words_5(string):
    """review solution final - count words in a sentence"""
    return Counter(re.findall(r"\b[\w'-]+\b", string.lower()))

