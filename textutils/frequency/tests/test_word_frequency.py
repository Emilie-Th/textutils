from textutils.frequency.word_frequency import word_frequency
import pytest


def test_word_frequency_normal():
    assert word_frequency("hello world hello") == {
        "hello": 2,
        "world": 1,
    }

def test_word_frequency_empty():
    assert word_frequency("") == {}

def test_word_frequency_whitespace():
    assert word_frequency("     ") == {}

def test_word_frequency_single_word():
    assert word_frequency("hello") == {
        "hello": 1,
    }  

def test_word_frequency_upper_false():
    assert word_frequency("Hello hello HELLO") == {
        "hello": 3,
    }


def test_word_frequency_upper_true():
    assert word_frequency("Hello hello HELLO", case_sensitive=True) == {
        "Hello": 1,
        "hello": 1,
        "HELLO": 1,
    }

def test_word_frequency_punctuation():
    assert word_frequency("Hello! hello. hello?") == {
        "hello": 3,
    }

def test_word_frequency_ignore_words():
    assert word_frequency("hello world hello", ignore_words=["hello"]) == {
        "world": 1,
        }

def test_word_frequency_min_length():
    assert word_frequency("I love Python", min_length=2) == {
        "love": 1,
        "python": 1,
    }

def test_word_frequency_top_n():
    assert word_frequency("cat dog cat bird cat dog", top_n=2) == {
        "cat": 3,
        "dog": 2,
    }


def test_word_frequency_top_n_zero():
    assert word_frequency("cat dog cat bird cat dog", top_n=0) == {}

def test_word_frequency_invalid_text():
    with pytest.raises(TypeError):
        word_frequency(123)


def test_word_frequency_negative_min_length():
    with pytest.raises(ValueError):
        word_frequency("hello world", min_length=-1)

def test_word_frequency_apostrophe():
    assert word_frequency("don't don't") == {"don't": 2}


def test_word_frequency_tied_frequencies():
    assert list(word_frequency("dog cat dog cat")) == ["dog", "cat"]


def test_word_frequency_ignore_words_case():
    assert word_frequency(
        "Hello hello world",
        ignore_words=["HELLO"],
    ) == {"world": 1}

def test_word_frequency_only_punctuation():
    assert word_frequency("!!! ??? ...") == {}