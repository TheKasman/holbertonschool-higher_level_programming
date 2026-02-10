#!/usr/bin/python3
"""
Lists the answer to the function that inherits_from a class
"""


def inherits_from(obj, a_class):
    """returns true if the object's class matches the search case"""
    return issubclass(obj.__class__, a_class)
