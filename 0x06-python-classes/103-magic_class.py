#!/usr/bin/python3

"""defines a magic class."""

import math


class MagicClass:
    """represntation of magic class

    Args:
        radius (int or float): the radius of magic class
    """
    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """calculates area"""
        return (self.__radius**2 * math.pi)

    def circumference(self):
        """calculates circumference"""
        return (2 * math.pi * self.__radius)
