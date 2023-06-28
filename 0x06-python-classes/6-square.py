#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """Representation of the square class."""

    def __init__(self, size=0, position=(0, 0)):
        """This initializes the square params.

        Args:
            size (int): The size of the square defined privately.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """gets the size attribute of square."""
        return (self.__size)

    @property
    def position(self):
        """gets the position attribute of square."""
        return (self.__position)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            if type(value[0]) != int or type(value[1]) != int:
                if value[0] < 0 or value[1] < 0:
                    raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

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
        if self.__size == 0:
            print("")
        else:
            [print("") for i in range(self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for n in range(self.__position[0])]
                [print("#", end="") for m in range(self.__size)]
                print("")
