#!/usr/bin/python3
"""
Module that returns the list of available attributes and methods of an object.
"""


#!/usr/bin/python3
"""Module that defines an is_same_class function"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class;
    otherwise False
    
    Args:
        obj: The object to check
        a_class: The class to check against
        
    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise
    """
    return type(obj) is a_class
