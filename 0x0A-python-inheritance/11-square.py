#!/usr/bin/python3
"""Defines a class Square."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square class."""

    def __init__(self, size):
        """initiates the class quare with size.
        instance.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """returns class representative in a print."""
        return "[Square] {}/{}".format(self.__width, self.__height)
