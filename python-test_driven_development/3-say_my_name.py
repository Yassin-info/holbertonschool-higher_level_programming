#!/usr/bin/python3
"""
Module that provides a function to print a name.

This module contains the say_my_name function which prints
a formatted name string.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first name> <last name>'.

    Args:
        first_name: The first name (must be a string)
        last_name: The last name (must be a string), default is ""

    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
