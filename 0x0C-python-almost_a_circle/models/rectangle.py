#!/usr/bin/python3
"""
Module for Rectangle class
"""
from models.base import Base

class Rectangle(Base):
    """
    Rectangle class inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x-coordinate of the rectangle (default is 0).
            y (int): y-coordinate of the rectangle (default is 0).
            id (int): If id is not None, assign it to the public instance attribute id.
                      Otherwise, use the id from the Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute

        Args:
            value (int): Value to set width to.
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter for height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute

        Args:
            value (int): Value to set height to.
        """
        self.__height = value

    @property
    def x(self):
        """
        Getter for x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x attribute

        Args:
            value (int): Value to set x to.
        """
        self.__x = value

    @property
    def y(self):
        """
        Getter for y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y attribute

        Args:
            value (int): Value to set y to.
        """
        self.__y = value
