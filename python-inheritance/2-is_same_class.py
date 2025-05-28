#!/usr/bin/python3
"""
Module containing a function to check exact class membership.

This function determines if an object is a direct instance of a specific
class, without considering inheritance relationships.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.
    
    This function uses type() instead of isinstance() to verify only
    direct class membership, excluding parent classes in the inheritance
    hierarchy. It performs strict type checking.
    
    Args:
        obj: The object to check
        a_class: The reference class for comparison
        
    Returns:
        bool: True if obj is exactly an instance of a_class,
              False in all other cases (including inheritance)
              
    Example:
        >>> is_same_class(1, int)
        True
        >>> is_same_class(1, object)  # Even though int inherits from object
        False
    """
    return type(obj) is a_class
