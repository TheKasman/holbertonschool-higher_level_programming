#!/usr/bin/python3
"""
0-add_integer.py
Module for adding two integers together with doctest examples
"""


def add_integer(a, b=98):
    """
    Adds two integers together and returns the result
    a and b must be integers (floats are truncated to integers)
    Raises TypeError for invalid inputs, including NaN or infinity.

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
    # Reject NaN for a
    if isinstance(a, float) and a != a:
        raise TypeError("a must be an integer")

    # Reject NaN for b
    if isinstance(b, float) and b != b:
        raise TypeError("b must be an integer")

    # Reject infinities for a
    if isinstance(a, float) and (a == float('inf') or a == float('-inf')):
        raise TypeError("a must be an integer")

    # Reject infinities for b
    if isinstance(b, float) and (b == float('inf') or b == float('-inf')):
        raise TypeError("b must be an integer")

    # Type checks
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

