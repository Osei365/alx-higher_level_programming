#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents the class student."""

    def __init__(self, first_name, last_name, age):
        """initiales student class."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dict rep of class instance."""
        if (type(attrs) == list and
                all(isinstance(i, str) for i in attrs)):
            return {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__.keys()}
        return self.__dict__

    def reload_from_json(self, json):
        """reload json to obj."""
        for key, value in json.items():
            setattr(self, key, value)
