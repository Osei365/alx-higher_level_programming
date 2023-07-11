#!/usr/bin/python3
"""Defines a function that writes
to a file.
"""


def write_file(filename="", text=""):
    """returns length of characters."""

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
