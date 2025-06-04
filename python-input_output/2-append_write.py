#!/usr/bin/python3
"""
Module containing a function to append text to files.

This module provides functionality to append strings to UTF-8 encoded
text files and return the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8) and returns the number
    of characters added.

    This function opens a file in append mode with UTF-8 encoding,
    writes the provided text to the end of it, and returns the count
    of characters added. The 'with' statement ensures proper file
    handling and automatic closure of the file.

    Args:
        filename (str): The path to the file to append to.
        Defaults to empty string.
        text (str): The text content to append to the file.
        Defaults to empty string.

    Returns:
        int: The number of characters added to the file.

    Note:
        - Creates the file if it doesn't exist
        - Appends to the end of the file if it already exists
        - File permission exceptions are not handled
        - Uses UTF-8 encoding for writing the file
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
