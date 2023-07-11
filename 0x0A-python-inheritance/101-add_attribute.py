#!/usr/bin/python3
"""defines a fucntion that adds an
attribute to an object.
"""


def add_attribute(obj, name, value):
    """adds value to attribute in object."""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
