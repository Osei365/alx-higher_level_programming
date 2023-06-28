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
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
           raise TypeError("position must be a tuple of 2 positive integers")
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
    def __str__(self):
        """This determines how class is displayed."""
        if self.__size == 0:
            return ("")
        header = ["\n" for i in range(self.__position[1])]
        dis_string = "".join(header)
        for i in range(self.__size):
            space = [" " for n in range(self.__position[0])]
            dis_string += "".join(space)
            row = ["#" for m in range(self.__size)]
            dis_string += "".join(row)
            dis_string += "\n"
        return (dis_string[:-1])
