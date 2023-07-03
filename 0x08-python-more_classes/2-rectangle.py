#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Represents rectangle class."""

    def __init__(self, width=0, height=0):
        """This initializes the width and height
        of the Rectangle class

        Args:
            width (int): width of rectangle
            height (int): height rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This gets the width attribute of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """This gets the height attribute of rect."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))
