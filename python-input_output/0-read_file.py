#!/usr/bin/python3
"""
Module containing a function to read and print text files.

This module provides functionality to read UTF-8 encoded text files
and print their contents to standard output.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.

    This function opens a file in read mode with UTF-8 encoding,
    reads its entire content, and prints it to standard output.
    The 'with' statement ensures proper file handling and automatic
    closure of the file.

    Args:
        filename (str): The path to the file to read. Defaults to empty string.

    Note:
        - File permission and file existence exceptions are not handled
        - Uses UTF-8 encoding for reading the file
        - Prints content directly without additional formatting
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
