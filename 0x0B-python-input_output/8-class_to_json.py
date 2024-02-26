#!/usr/bin/python3
"""Module to convert a class instance to a JSON-serializable dictionary"""

def class_to_json(obj):
    """Return the dictionary description of a JSON-serializable object"""
    return obj.__dict__
