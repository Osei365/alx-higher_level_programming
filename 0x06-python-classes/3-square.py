#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """Representation of the square class."""

    def __init__(self, size=0):
        """This initializes the square params.

        Args:
            size (int): The size of the square defined privately.
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """This claculates the area of the square object.

        Returns:
            The are of the square
        """
        return (self.__size**2)
