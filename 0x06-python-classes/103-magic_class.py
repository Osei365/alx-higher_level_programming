#!/usr/bin/python3
import math
"""defines a magic class."""


class MagicClass:
    """represntation of magic class."""

    def __init__(self, radius):
        self.radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.radius = radius

    def area(self):
        """calculates area"""
        return (self.radius**2 * math.pi)

    def circumference(self):
        """calculates circumference"""
        return (2 * math.pi * self.radius)
