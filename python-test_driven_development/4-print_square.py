#!/usr/bin/python3
"""
Module that provides a function to print a square.

This module contains the print_square function which prints
a square using the '#' character.
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size: The size length of the square (must be an integer >= 0)

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
