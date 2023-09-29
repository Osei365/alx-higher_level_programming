#!/usr/bin/python3
"""get peak."""


def find_peak(list_of_integers):
    """calculates the peak in the array."""

    max_ele = None
    for el in list_of_integers:
        if max_ele is None or max_ele < el:
            max_ele = el
    return max_ele
