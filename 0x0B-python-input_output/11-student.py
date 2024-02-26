#!/usr/bin/python3
"""Module to define the Student class"""

class Student:
    """Class to represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary description of a Student instance"""
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with a given dictionary"""
        self.__dict__.update(json)
