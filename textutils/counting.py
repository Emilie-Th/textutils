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
    
