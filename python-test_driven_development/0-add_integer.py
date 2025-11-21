#!/usr/bin/python3
"""
Module that provides a function to add two integers.

This module contains the add_integer function which adds two numbers
after ensuring they are integers or can be converted to integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers together.

    Args:
        a: First number (int or float)
        b: Second number (int or float), default is 98

    Returns:
        The addition of a and b as an integer

    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        if a != a or a == float('inf') or a == float('-inf'):
            raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float):
        if b != b or b == float('inf') or b == float('-inf'):
            raise ValueError("cannot convert float NaN to integer")
    return int(a) + int(b)
