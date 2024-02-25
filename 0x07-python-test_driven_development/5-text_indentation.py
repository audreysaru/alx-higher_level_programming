#!/usr/bin/python3
"""
This is the 5-text_indentation module.
It defines a function for text indentation.
"""

def text_indentation(text):
    """
    Prints text with indentation.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in separators:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line:
        print(current_line.strip())
