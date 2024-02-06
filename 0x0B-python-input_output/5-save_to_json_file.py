#!/usr/bin/python3
"""A function that writes an Object to a text file,
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as p:
        json.dump(my_obj, p)
