#!/usr/bin/python3
"""defines a function that creates
and appends to a file."""


def append_write(filename="", text=""):
    """returns number of characters in string."""

    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
    return len(text)
