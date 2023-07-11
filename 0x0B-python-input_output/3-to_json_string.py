#!/usr/bin/python3
"""defines a function that gets the JSON
string rep of an object in Python.
"""

import json


def to_json_string(my_obj):
    """returns JSON string representation."""

    return json.dumps(my_obj)
