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
    for i in range(len(text)):
        if text[i] == " " and text[i-1] in ".?:":
            continue
        else:
            print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
