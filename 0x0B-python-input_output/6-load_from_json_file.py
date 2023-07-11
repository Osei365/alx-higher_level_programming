#!/usr/bin/python3
"""Defines adeserialize a file that
has JSON format."""


import json


def load_from_json_file(filename):
    """deserializes a file into an object."""

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
