#!/usr/bin/python3
"""A function that creates an Object from a “JSON file”."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as p:
        return json.load(p)
