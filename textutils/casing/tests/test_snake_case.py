from textutils.casing.snake_case import snake_case


def test_snake_case_normal():
    assert snake_case("hello world") == "hello_world"


def test_snake_case_upper():
    assert snake_case("HELLO WORLD") == "hello_world"


def test_snake_case_multiple_spaces():
    assert snake_case("hello   world") == "hello_world"


def test_snake_case_empty():
    assert snake_case("") == ""


def test_snake_case_already_snake_case():
    assert snake_case("hello_world") == "hello_world"


def test_snake_case_newlines():
    assert snake_case("hello\nworld") == "hello_world"


def test_snake_case_tabs():
    assert snake_case("hello\tworld") == "hello_world"


def test_snake_case_leading_trailing_spaces():
    assert snake_case(" hello world ") == "hello_world"
