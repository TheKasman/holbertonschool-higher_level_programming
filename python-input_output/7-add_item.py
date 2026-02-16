#!/usr/bin/python3
"""Now we load add and save things...importing all the other files required"""
import sys
saved = __import__('5-save_to_json_file').save_to_json_file
loaded = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """Adding items"""
    args = sys.argv[1:]
    data = loaded("add_item.json")

    if data is None:
        data = []

    for x in args:
        data.append(x)

    saved(data, "add_item.json")

if __name__ == "__main__":
    add_item()