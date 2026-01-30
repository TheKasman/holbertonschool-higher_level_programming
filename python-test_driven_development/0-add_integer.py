#!/usr/bin/python3
"""
0-add_integer.py
Module for adding two integers together with doctest examples
"""


def add_integer(a, b=98):
    """
    Adds two integers together and returns the result
    a and b must be integers (floats are truncated to integers)

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
    TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)) or a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
