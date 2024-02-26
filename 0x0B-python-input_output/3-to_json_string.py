#!/usr/bin/python3
"""Module defining the to_json_string function"""
import json

def to_json_string(my_obj):
    """Return the JSON representation of an object (string)"""
    return json.dumps(my_obj)
