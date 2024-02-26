#!/usr/bin/python3
"""Module defining the from_json_string function"""
import json

def from_json_string(my_str):
    """Return the Python data structure represented by a JSON string"""
    return json.loads(my_str)
