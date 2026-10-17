from textutils.casing.capitalize_words import capitalize_words


def test_capitalize_words_normal():
    assert capitalize_words("hello world") == "Hello World"


def test_capitalize_words_capitalize():
    assert capitalize_words("Hello World") == "Hello World"


def test_capitalize_words_upper():
    assert capitalize_words("HELLO WORLD") == "HELLO WORLD"


def test_capitalize_words_empty():
    assert capitalize_words("") == ""


def test_capitalize_words_number():
    assert capitalize_words("1234") == "1234"


def test_capitalize_words_multiple_spaces():
    assert capitalize_words("hello   world") == "Hello   World"


def test_capitalize_words_newlines():
    assert capitalize_words("hello\nworld") == "Hello\nWorld"


def test_capitalize_words_tabs():
    assert capitalize_words("hello\tworld") == "Hello\tWorld"


def test_capitalize_words_apostrophe():
    assert capitalize_words("don't stop") == "Don't Stop"
