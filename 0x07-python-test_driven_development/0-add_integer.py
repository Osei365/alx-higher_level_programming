#!/usr/bin/python3
"""Define a function that adds two integers"""


def add_integer(a, b=98):
    """This function adds two numbers.

    Float arguments must be coverted to int upon addition.

    Raises:
        TypeError: if a or b are not int or floats
    """

    a_check = isinstance(a, (int, float))
    b_check = isinstance(b, (int, float))
    if not a_check:
        raise TypeError('a must be an integer')
    elif not b_check:
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
