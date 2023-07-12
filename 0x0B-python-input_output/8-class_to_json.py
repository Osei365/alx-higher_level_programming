#!/usr/bin/python3
"""Defines a function that returns
dict of a class obj."""


def class_to_json(obj):
    """returns dict rep of a class obj in json.
    serialization."""

    return obj.__dict__
