#!/usr/bin/python3
"""
Module containing a function to write text to files.

This module provides functionality to write strings to UTF-8 encoded
text files and return the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number
    of characters written.

    This function opens a file in write mode with UTF-8 encoding,
    writes the provided text to it, and returns the count of characters
    written. The 'with' statement ensures proper file handling and
    automatic closure of the file.

    Args:
        filename (str): The path to the file to write.
        Defaults to empty string.
        text (str): The text content to write to the file.
        Defaults to empty string.

    Returns:
        int: The number of characters written to the file.

    Note:
        - Creates the file if it doesn't exist
        - Overwrites the content if the file already exists
        - File permission exceptions are not handled
        - Uses UTF-8 encoding for writing the file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
