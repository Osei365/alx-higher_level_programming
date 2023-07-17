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
                list_dictionaries == [] or
                not all(isinstance(item, dict) for item in list_dictionaries)):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves file with json object"""
        if list_objs is not None:
            list_dict = [r.to_dictionary() for r in list_objs]
        else:
            list_dict = []
        with open("{}.json".format(cls.__name__), "w") as f:
            json_repr = cls.to_json_string(list_dict)
            f.write(json_repr)
