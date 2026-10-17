import string


def _normalize(word, case_sensitive):
    """
    Strip surrounding punctuation and apply the case option to a word.

    Parameters
    ----------
    word : str
        The word to clean.
    case_sensitive : bool
        If False, the word is converted to lowercase.

    Returns
    -------
    str
        The cleaned word, which may be empty if it contained
        only punctuation.
    """
    word = word.strip(string.punctuation)
    return word if case_sensitive else word.lower()


def _normalize_ignored(ignore_words, case_sensitive):
    """
    Build the set of words to ignore, following the case option.

    Parameters
    ----------
    ignore_words : list[str] or None
        Words to exclude, or None for no exclusion.
    case_sensitive : bool
        If False, ignored words are converted to lowercase.

    Returns
    -------
    set[str]
        The normalized words to ignore.
    """
    return {_normalize(word, case_sensitive) for word in (ignore_words or [])}


def _extract_words(text, case_sensitive, ignored, min_length):
    """
    Yield the words of a text that must be counted.

    Parameters
    ----------
    text : str
        The text to analyze.
    case_sensitive : bool
        Whether to preserve the original case.
    ignored : set[str]
        Normalized words to skip.
    min_length : int
        Words shorter than this are skipped.

    Yields
    ------
    str
        Each normalized word that passes the filters.
    """
    for raw_word in text.split():
        word = _normalize(raw_word, case_sensitive)
        if word and len(word) >= min_length and word not in ignored:
            yield word


def _count_words(words):
    """
    Count word occurrences, keeping the order of first appearance.

    Parameters
    ----------
    words : Iterable[str]
        The words to count.

    Returns
    -------
    dict[str, int]
        The number of occurrences of each word.
    """
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def _sort_by_frequency(counts):
    """
    Sort word counts by decreasing frequency.

    Words with equal frequencies keep their order of first appearance.

    Parameters
    ----------
    counts : dict[str, int]
        The number of occurrences of each word.

    Returns
    -------
    list[tuple[str, int]]
        The (word, count) pairs, ordered by decreasing frequency.
    """
    return sorted(counts.items(), key=lambda item: -item[1])


def word_frequency(
    text, case_sensitive=False, ignore_words=None, min_length=1, top_n=None
):
    """
    Count how often each word appears in a text.

    Punctuation around words is ignored, so "python", "python." and "python!"
    are the same word. Apostrophes inside a word (e.g. "don't") are kept.

    Parameters
    ----------
    text : str
        The text to analyze.
    case_sensitive : bool, optional
        If False (default), "Python" and "python" are counted as the
        same word and returned in lowercase.
    ignore_words : list[str] or None, optional
        Words to exclude from the result.
        The comparison follows the case_sensitive option.
    min_length : int, optional
        Words shorter than this are ignored. Defaults to 1.
    top_n : int or None, optional
        If set, only the top_n most frequent words are returned.
        Defaults to None.

    Returns
    -------
    dict[str, int]
        A dictionary ordered by decreasing frequency. Words with
        the same frequency keep their order of first appearance.
        An empty or whitespace-only text returns an empty dictionary.

    Raises
    ------
    TypeError
        If text is not a string.
    ValueError
        If min_length is negative.

    Examples
    --------
    >>> word_frequency("Python is great. Python is simple.")
    {'python': 2, 'is': 2, 'great': 1, 'simple': 1}
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if min_length < 0:
        raise ValueError("min_length must be greater than or equal to 0")
    if top_n is not None and top_n <= 0:
        return {}

    ignored = _normalize_ignored(ignore_words, case_sensitive)
    words = _extract_words(text, case_sensitive, ignored, min_length)
    ordered = _sort_by_frequency(_count_words(words))
    return dict(ordered[:top_n])
