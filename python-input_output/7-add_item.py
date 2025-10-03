#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list
and saves them to a file in JSON format.
"""


import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

args = sys.argv[1:]

try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []

my_list.extend(args)
save_to_json_file(my_list, "add_item.json")
