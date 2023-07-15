#!/usr/bin/python3
"""Defines a class Base."""


class Base:
    """Represents a class base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """initiates the class with id
        public instance variable"""

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
