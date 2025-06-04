#!/usr/bin/python3
"""
Module containing a function to convert objects to JSON strings.

This module provides functionality to serialize Python objects
into JSON string representation.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    
    This function takes a Python object and converts it to its
    JSON string representation using the json.dumps() method.
    
    Args:
        my_obj: The Python object to be serialized to JSON string.
                Can be any JSON-serializable object (dict, list, str, 
                int, float, bool, None).
        
    Returns:
        str: The JSON string representation of the object.
        
    Note:
        - Does not handle exceptions if the object can't be serialized
        - Objects like sets, custom classes, etc. will raise TypeError
        - JSON serializable types: dict, list, tuple, str, int, float, bool, None
    """
    return json.dumps(my_obj)
