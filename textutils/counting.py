def word_count(text):
    """
    Count the number of words in a text.

     Args:
     text (str): The text in which to count the words.

     Returns:
     int: The number of words in the text.
     """
    words = text.split()
    return len(words)
    


def character_count(text, include_spaces=True):
    """
    Count the number of characters in a text.

    Args:
    text (str): The text in which to count the characters.
    include_spaces (bool): Whether to include spaces in the count. Defaults to True.

    Returns:
    int: The number of characters in the text.
    """
    if not include_spaces:
        nb = 0
        for i in range(len(text)):
            if text[i] != " ":
                nb += 1
        return nb 
    else:
        return len(text)