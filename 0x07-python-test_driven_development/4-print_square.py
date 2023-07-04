#!/usr/bin/python3
"""Defines a functions that prints a square."""


def print_square(size):
    """This prints a square.

    Args:
        size (int): the size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
        TypeError: if size is a float and less than zero.
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for _ in range(size):
        [print("#", end="") for i in range(size)]
        print("")
