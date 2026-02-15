#!/usr/bin/python3

"""Writing this down... to write a file"""


def write_file(filename="", text=""):
    """I would never have guessed what this does!?"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
