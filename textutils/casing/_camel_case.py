def camel_case(text):
    """
    Convert a text to camel case.

    Parameters
    ----------
    text : str
        The text to convert to camel case.

    Returns
    -------
    str
        The text converted to camel case.
    """
    words = text.split()

    if not words:
        return ""

    return words[0].lower() + "".join(word.capitalize() for word in words[1:])
