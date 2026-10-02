def snake_case(text):
    """
    Convert a text to snake case.

    Args:
    text (str): The text to convert to snake case.
    
    Returns:
    str: The text converted to snake case.
    """
    return "_".join(text.lower().split())