#!/usr/bin/python3
"""
Module that provides a function to divide a matrix.

This module contains the matrix_divided function which divides all
elements of a matrix by a divisor and returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats
        div: The number to divide by (int or float)

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimals

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows of matrix are not the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is zero
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
