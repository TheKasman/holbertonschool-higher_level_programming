#!/usr/bin/python3

"""This file.... append to it."""


def write_file(filename="", text=""):
    """Append to it"""
    with open(filename, "a", encoding="utf-8") as f:
        num_chars = f.write(text)
    return num_chars
