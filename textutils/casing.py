def capitalize_words(text):
    """
    Capitalize the first letter of each word in a text.

    Args:
    text (str): The text in which to capitalize the words.

    Returns:
    str: The text with each word capitalized.
    """
    result=""
    for i in range(len(text)):
        if i == 0 or text[i - 1] == " ":
            result += text[i].upper()
        else:
            result += text[i]
    return result
