#!/usr/bin/python3

"""
Prints two new lines after ever . ? and :

Args:
    text: the text we're modifying
"""


def text_indentation(text):
    """
    >>> text_indentation(123)
    Traceback (most recent call last):
    TypeError: text must be a string

    >>> text_indentation("Lorem ipsum:")
    Lorem ipsum:

    >>> text_indentation("Lorem ipsum: why")
    Lorem ipsum:

    why
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = False

    for idx, char in enumerate(text):
        if skip_space and char == " ":
            continue

        skip_space = False
        print(char, end="")

        if char in ".?:":
            if idx != len(text) - 1:
                print("\n")
                skip_space = True
