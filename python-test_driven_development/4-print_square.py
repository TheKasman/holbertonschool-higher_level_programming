#!/usr/bin/python3

"""
Prints a Square using #

Args:
    size: the size of the square we want
"""

def print_square(size):

    """
    >>> print_square(3)
    ###
    ###
    ###
    >>> print_square(-1)
    Traceback (most recent call last):
    ValueError: size must be >= 0
    >>> print_square(3.5)
    ###
    ###
    ###
    >>> print_square(-3.5)
    Traceback (most recent call last):
    TypeError: size must be an integer
    >>> print_square('fifty')
    Traceback (most recent call last):
    TypeError: size must be an integer
    """

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    
    if isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")
    
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    size = int(size)
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
