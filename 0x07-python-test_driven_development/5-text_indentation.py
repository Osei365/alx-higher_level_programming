#!/usr/bin/python3
"""Define a function that modifies a string."""


def text_indentation(text):
    """modifies a text/string.

     adds two new lines after . ?, and :

    Args:
        text (str): string to be modified.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".:?":
            if text[i] in ".:?":
                print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
