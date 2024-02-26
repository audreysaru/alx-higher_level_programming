#!/usr/bin/python3
"""Script to add command line arguments to a list and save it to a JSON file"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_item(args):
    """Add command line arguments to a list and save to a JSON file"""
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(args[1:])
    save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    add_item(sys.argv)
