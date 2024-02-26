#!/usr/bin/python3
"""Module defining the read_file function"""

def read_file(filename=""):
    """Read a text file and print its contents to stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
