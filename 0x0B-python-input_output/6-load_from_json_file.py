#!/usr/bin/python3
"""Module defining the load_from_json_file function"""
import json

def load_from_json_file(filename):
    """Create an object from a JSON file"""
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
