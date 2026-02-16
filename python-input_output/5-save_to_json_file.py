#!/usr/bin/python3
"""Now we save to a json file"""
import json


def save_to_json_file(my_obj, filename):
    """The thing that makes us save it"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
