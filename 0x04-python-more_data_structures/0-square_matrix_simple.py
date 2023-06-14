#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        result = [[n**2 for n in i] for i in matrix]
        return (result)
    return (matrix)
