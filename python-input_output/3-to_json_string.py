#!/usr/bin/python3
"""
This module provides a function that converts a Python object to a JSON string.
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object.

    Args:
        my_obj: The Python object to be serialized.

    Returns:
        str: A JSON-formatted string representing the object.
    """
    json_string = json.dumps(my_obj)
    return json_string
