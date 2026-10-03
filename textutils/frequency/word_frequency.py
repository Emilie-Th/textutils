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


def _normalize_ignored(ignore_words, case_sensitive):
    """
    Build the set of words to ignore, following the case option.

    Args:
        ignore_words (list[str] | None): Words to exclude, or None for no exclusion.
        case_sensitive (bool): If False, ignored words are lowercased.

    Returns:
        set[str]: The normalized words to ignore.
    """
    return {_normalize(word, case_sensitive) for word in (ignore_words or [])}


def _extract_words(text, case_sensitive, ignored, min_length):
    """
    Yield the words of a text that must be counted.

    Args:
        text (str): The text to analyze.
        case_sensitive (bool): Whether the case is kept as is.
        ignored (set[str]): Normalized words to skip.
        min_length (int): Words shorter than this are skipped.

    Yields:
        str: Each normalized word that passes the filters.
    """
    for raw_word in text.split():
        word = _normalize(raw_word, case_sensitive)
        if word and len(word) >= min_length and word not in ignored:
            yield word
