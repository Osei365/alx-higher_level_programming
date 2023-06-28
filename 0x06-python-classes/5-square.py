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

    def my_print(self):
        """This prints the square using hash.

        Returns:
            nothing
        """
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for n in range(self.size):
                    if n == self.size - 1:
                        print('#')
                    else:
                        print('#', end="")
