from textutils.transform.reverse import reverse


def test_reverse_normal():
    assert reverse("bonjour") == "ruojnob"


def test_reverse_empty():
    assert reverse("") == ""


def test_reverse_single_character():
    assert reverse("a") == "a"


def test_reverse_with_spaces():
    assert reverse("hello world") == "dlrow olleh"

def test_reverse_unicode():
    assert reverse("été") == "été"


def test_reverse_numbers():
    assert reverse("12345") == "54321"