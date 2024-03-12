#!/usr/bin/python3
"""
Module for Base class
"""

class Base:
    """
    Base class for managing id attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class

        Args:
            id (int): If id is not None, assign it to the public instance attribute id.
                      Otherwise, increment __nb_objects and assign the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
