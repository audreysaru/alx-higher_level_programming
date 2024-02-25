#!/usr/bin/python3
"""Module defining the Square class"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Class representing a square"""

    def __init__(self, size):
        """Initialize a Square instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square"""
        return super().area()

    def __str__(self):
        """Return a string representation of the square"""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
