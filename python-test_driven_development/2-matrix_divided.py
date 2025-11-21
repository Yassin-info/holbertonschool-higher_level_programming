#!/usr/bin/python3
"""
Module that divides a matrix.

This module contains the matrix_divided function.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix and returns a new matrix.

    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(error_msg)

    if not all(len(row) > 0 for row in matrix):
        raise TypeError(error_msg)

    if not all(isinstance(elem, (int, float))
               for row in matrix for elem in row):
        raise TypeError(error_msg)

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
