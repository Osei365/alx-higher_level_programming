#!/usr/bin/python3i
"""Defines a function that.
prints the firtname and lasname
of an individual.
"""


def say_my_name(first_name, last_name=""):
    """This prints the firstname and
    last name of individual.

    Args:
        first_name (str): the first name
        last_name (str): the last name

    Raises:
        TypeError: If first and last name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("my name is {} {}".format(first_name, last_name))
