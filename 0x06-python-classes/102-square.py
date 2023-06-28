#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """Representation of the square class."""

    def __init__(self, size=0):
        """This initializes the square params.

        Args:
            size (int): The size of the square defined privately.
        """
        self.size = size

    @property
    def size(self):
        """gets the size attribute of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """This claculates the area of the square object.

        Returns:
            The are of the square
        """
        return (self.__size**2)

    def __eq__(self, other):
        """equal to comparison"""
        return self.area() == other.area()

    def __ne__(self, other):
        """not equal to comparison"""
        return self.area() != other.area()

    def __lt__(self, other):
        """less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """less than and eqaul to"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """greater than comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """greater than and equal to"""
        return self.area() >= other.area()
