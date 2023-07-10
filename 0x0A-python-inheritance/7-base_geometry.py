#!/usr/bin/python3
"""Defines a class Geometry."""


class BaseGeometry:
    """Represents the BasGeometry class."""

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this validates an integer.
        Raises:
            TypeError: value is not an integer.
            ValueError: value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
