#!/usr/bin/python3
"""
This module defines a function is_same_class.
"""

def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj (any): The object to be checked.
        a_class (class): The specified class.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
