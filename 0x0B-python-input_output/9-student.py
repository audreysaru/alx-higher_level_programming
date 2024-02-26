#!/usr/bin/python3
"""Module to define the Student class"""

class Student:
    """Class to represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary description of a Student instance"""
        return self.__dict__
