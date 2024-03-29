#!/usr/bin/python3
"""
This module defines a function that adds two integers and writes the result to a file.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer. Defaults to 98 if not provided.

    Raises:
        TypeError: If a or b is not an integer.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
