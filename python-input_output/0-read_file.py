#!/usr/bin/python3

"""Time to read input from a file"""


def read_file(filename=""):
    """You guessed it. we're reading from a file"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    return read_data
