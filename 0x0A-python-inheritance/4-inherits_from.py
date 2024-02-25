#!/usr/bin/python3
"""
This module defines a function inherits_from.
"""

def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj (any): The object to be checked.
        a_class (class): The specified class.

    Returns:
        bool: True if obj is an instance of a class that inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
