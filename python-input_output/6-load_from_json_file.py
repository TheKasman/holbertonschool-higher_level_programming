#!/usr/bin/python3
"""Now we take a file and make an object"""
import json


def load_from_json_file(filename):
    """take the file, and make the object"""
    with open(filename, "r", encoding="utf-8") as f:
        object = json.load(f)
    return object
