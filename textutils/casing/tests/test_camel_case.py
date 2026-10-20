from textutils.casing._camel_case import camel_case


def test_camel_case_normal():
    assert camel_case("hello world") == "helloWorld"


def test_camel_case_upper():
    assert camel_case("HELLO WORLD") == "helloWorld"


def test_camel_case_multiple_spaces():
    assert camel_case("hello   world") == "helloWorld"


def test_camel_case_empty():
    assert camel_case("") == ""


def test_camel_case_newlines():
    assert camel_case("hello\nworld") == "helloWorld"


def test_camel_case_tabs():
    assert camel_case("hello\tworld") == "helloWorld"


def test_camel_case_leading_trailing_spaces():
    assert camel_case(" hello world ") == "helloWorld"
