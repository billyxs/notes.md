# https://www.pythonmorsels.com/exercises/33b4af3082734d00bc62effc8da16375/

from collections import Counter
import re
from unidecode import unidecode
from unicodedata import normalize

def is_anagram__(a, b):
    """compare two words to see if they are anagrams"""

    def get_string(string):
        return sorted(unidecode(
            re.sub(r'\W+', '', string.lower())
        ))

    return get_string(a) == get_string(b)


# Solutions

def is_anagram_1(word1, word2):
    """Return True if the given words are anagrams"""
    word1, word2 = word1.lower(), word2.lower()
    return sorted(word1) == sorted(word2)


def is_anagram_2(word1, word2):
    """Return True if the given words are anagrams"""
    word1, word2 = word1.lower(), word2.lower()
    return Counter(word1.replace(' ', '')) == Counter(word2.replace(' ', ''))


def is_anagram_3(word1, word2):
    """Return True if the given words are anagrams"""
    word1, word2 = word1.lower(), word2.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters1 = sorted(c for c in word1 if c in alphabet)
    letters2 = sorted(c for c in word2 if c in alphabet)
    return letters1 == letters2


def is_anagram_4(word1, word2):
    """Return True if the given words are anagrams"""
    word1, word2 = word1.lower(), word2.lower()
    letters1 = sorted(c for c in word1 if c.isalpha())
    letters2 = sorted(c for c in word2 if c.isalpha())
    return letters1 == letters2


def is_anagram_5(word1, word2):
    """Return True if the given words are anagrams"""
    word1, word2 = word1.lower(), word2.lower()
    letters1 = sorted(c for c in word1 if c.isalpha())
    letters2 = sorted(c for c in word2 if c.isalpha())
    return letters1 == letters2


def is_anagram_6(word1, word2):
    """Return True if the given words are anagrams"""
    def count_letters(string):
        return Counter(
            char
            for char in string.lower() if char.isalpha()
        )
    return count_letters(word1) == count_letters(word2) 


def is_anagram(word1, word2):
    """Return True if the given words are anagrams"""
    def count_letters(string):
        string = normalize('NFKD', string.lower())
        return sorted(
            char
            for char in string.lower() if char.isalpha()
        )
    return count_letters(word1) == count_letters(word2) 
