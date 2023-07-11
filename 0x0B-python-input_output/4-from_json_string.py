#!/usr/bin/python3
"""Defines a function that deserializes a
JSON string.
"""

import json


def from_json_string(my_str):
    """returns a deserialized JSON object."""

    return json.loads(my_str)
