#!/usr/bin/python3

"""Lookup function docstring"""


def lookup(obj):
    """Gets every attribute from the object and puts it in a list"""
    list = {}
    for attr in dir(obj):
        list[attr] = getattr(obj, attr)
    return list
