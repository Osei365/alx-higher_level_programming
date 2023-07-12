#!/usr/bin/python3
"""Defines a function that inserts and updates"""


def append_after(filename="", search_string="", new_string=""):
    """inserts text into lines passing
    some search criteria."""

    new_lines = []
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
    with open(filename, 'w', encoding="utf-8") as f:
        f.writelines(new_lines)
