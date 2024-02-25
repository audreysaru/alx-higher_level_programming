#!/usr/bin/python3

"""
Module to provide a function for looking up attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list containing the names of attributes and methods.
    """
    return dir(obj)
