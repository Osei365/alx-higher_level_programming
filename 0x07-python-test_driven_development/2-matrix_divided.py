#!/usr/bin/python3
"""Defines a function that divides a matrix."""


def matrix_divided(matrix, div):
    """This divides a matrix.

    Returns:
       a new matrix
    """
    if (not isinstance(matrix, list) or
                len(matrix) < 2 or
                not all(isinstance(item, list) for item in matrix) or
                not all(isinstance(num, (int, float)) for item in matrix for num in item)):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    first_len = len(matrix[0])
    if (not all(len(itm_len) == first_len for itm_len in matrix[1:])):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = [[round(i/div, 2) for i in item] for item in matrix]
    return new_matrix
