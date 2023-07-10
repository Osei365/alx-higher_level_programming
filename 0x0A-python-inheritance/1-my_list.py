#!/usr/bin/python3
"""Defines a class that inherits from.
a list.
"""


class MyList(list):
    """Represents the mylist class."""

    def print_sorted(self):
        """Prints the list out sorted."""

        print(sorted(self))
