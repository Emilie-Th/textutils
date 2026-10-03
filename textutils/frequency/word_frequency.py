import string


def _normalize(word, case_sensitive):
    """
    Strip surrounding punctuation and apply the case option to a word.

    Args:
        word (str): The word to clean.
        case_sensitive (bool): If False, the word is converted to lowercase.

    Returns:
        str: The cleaned word (may be empty if it only contained punctuation).
    """
    word = word.strip(string.punctuation)
    return word if case_sensitive else word.lower()
