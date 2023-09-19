
from lib.count_words import *

#if given an empty string, it returns an empty string.

def test_count_words():
    pass

def test_count_words_five_words():
    result = count_words("Hello I like apples alot")
    assert result == 5

def test_count_words_no_words():
    result = count_words("")
    assert result == 0
