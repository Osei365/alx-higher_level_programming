#!/usr/bin/python3
"""Defines a function that checks if an
object is a child of another object.
"""


def is_same_class(obj, a_class):
    """returns True if object is
    in a child else False."""

    if type(obj) == a_class:
        return True
    else:
        return False
