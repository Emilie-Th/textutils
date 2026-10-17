from textutils.counting.word_count import word_count


def test_word_count_normal():
    assert word_count("Hello world") == 2


def test_word_count_empty():
    assert word_count("") == 0


def test_word_count_single_word():
    assert word_count("Hello") == 1


def test_word_count_multiple_spaces():
    assert word_count("Hello   world") == 2


def test_word_count_whitespace():
    assert word_count("   ") == 0


def test_word_count_newlines():
    assert word_count("Hello\nworld") == 2


def test_word_count_tabs():
    assert word_count("Hello\tworld") == 2
