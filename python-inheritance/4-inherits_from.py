#!/usr/bin/python3
"""Module that defines a function to check if an object
inherits (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that
    inherited (directly or indirectly) from a_class.
    Otherwise, return False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
