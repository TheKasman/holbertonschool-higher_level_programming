#!/usr/bin/python3
""" we did to json, now we read the json"""
import json


def from_json_string(my_str):
    """As the module comment says, from json to string"""
    return json.loads(my_str)
