#!/usr/bin/python3
"""defines a function that
checks for a subclass.
"""


def inherits_from(obj, a_class):
    """returns True if subclass, else
     False.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
