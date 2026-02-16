#!/usr/bin/python3
import json
saved = __import__('5-save_to_json_file').save_to_json_file()
loaded = __import__('6-load_from_json_file').load_from_json_file()
"""Now we load add and save things...
importing all the other files required"""


def add_item(text=""):
    """Adding items"""
    data = loaded("add_item.json")

    if data is None:
        data = []

    data.append(text)

    saved(data, "add_item.json")
