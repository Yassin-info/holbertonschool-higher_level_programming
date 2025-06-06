#!/usr/bin/python3
"""Module that defines a function to load an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file

    Args:
        filename (str): Name of the JSON file to read from

    Returns:
        object: Python object created from the JSON file
    """
    with open(filename, 'r') as f:
        return json.load(f)
