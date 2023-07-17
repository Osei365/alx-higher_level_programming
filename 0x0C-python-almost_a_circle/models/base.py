#!/usr/bin/python3
"""Defines a class Base."""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts dictionary object to json"""

        if (list_dictionaries is None or
                list_dictionaries == []):
            return "[]"
        else:
            return json.dumps(list_dictionaries)
