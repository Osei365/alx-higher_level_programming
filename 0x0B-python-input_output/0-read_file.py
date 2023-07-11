#!/usr/bin/python3
"""defines a function to read a file."""


def read_file(filename=""):
    """prints out a text file.
    to stdout."""

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
