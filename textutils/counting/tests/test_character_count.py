from textutils.counting.character_count import character_count


def test_character_count():
    assert character_count("Hello world") == 11

def test_character_count_normal_true():
    assert character_count("Hello world", True) == 11

def test_character_count_normal_false():
    assert character_count("Hello world", False) == 10

def test_character_count_empty_true():
    assert character_count("", True) == 0

def test_character_count_empty_false():
    assert character_count("", False) == 0

def test_character_count_single_word_true():
    assert character_count("Hello", True) == 5

def test_character_count_single_word_false():
    assert character_count("Hello", False) == 5    

def test_character_count_multiple_spaces_true():
    assert character_count("Hello   world", True) == 13

def test_character_count_multiple_spaces_false():
    assert character_count("Hello   world", False) == 10

def test_character_count_whitespace_true():
    assert character_count("   ", True) == 3

def test_character_count_whitespace_false():
    assert character_count("   ", False) == 0

def test_character_count_newlines_true():
    assert character_count("Hello\nworld", True) == 11

def test_character_count_newlines_false():
    assert character_count("Hello\nworld", False) == 11

def test_character_count_tabs_true():
    assert character_count("Hello\tworld", True) == 11

def test_character_count_tabs_false():
    assert character_count("Hello\tworld", False) == 11
