#!/usr/bin/python3
"""Now we splat a class to json"""


def class_to_json(obj):
    """Get the class, and put it in a box"""
    return obj.__dict__()
