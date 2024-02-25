#!/usr/bin/python3
"""
This module defines a function is_kind_of_class.
"""

def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance of
    a class that inherited from, the specified class.

    Args:
        obj (any): The object to be checked.
        a_class (class): The specified class.

    Returns:
        bool: True if obj is an instance of a_class or its subclasses, False otherwise.
    """
    return isinstance(obj, a_class)
