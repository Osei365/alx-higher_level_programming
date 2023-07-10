#!/usr/bin/python3
"""Defines a class Rectangle."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents the rectangle class."""

    def __init__(self, width, height):
        """Initiates the class with instances."""
        self.__width = width
        self.__height = height
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
