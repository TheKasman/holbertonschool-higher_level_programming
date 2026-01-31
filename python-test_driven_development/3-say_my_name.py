#!/usr/bin/python3

"""
Prints first and last name
Args:
    first_name: a string of the first name
    last_name: a string of the last name
Returns:
    returns  of first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    >>> say_my_name("Walter", "White")
    My name is Walter White

    >>> say_my_name(12, "oh no")
    Traceback (most recent call last):
    TypeError: first_name must be a string

    >>> say_my_name("Bob")
    My name is Bob

    >>> say_my_name()
    Traceback (most recent call last):
    TypeError: say_my_name() missing 1
      required positional argument: 'first_name'
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("first_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
