#!/usr/bin/python3
"""Defines a class My int."""


class MyInt(int):
    """represents the MyInt class."""

    def __eq__(self, obj):
        """equal to method."""
        return not self.real == obj

    def __ne__(self, obj):
        """not equal to method."""
        return self.real == obj
