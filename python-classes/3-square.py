#!/usr/bin/python3
"""This module defines the Square class again.. again?"""


class Square:
    """The Square class NOW WITH DEFINED SIZE"""
    def __init__(self, size=0):
        """Constructor for a new square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Prints the current area of the square"""
    def area(self):
        print(self.__size)
