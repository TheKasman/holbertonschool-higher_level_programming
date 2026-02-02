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

    def area(self):
        """Prints the current area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using #"""
        if self.size == 0:
            print()
            return
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
        print()

    #  SIZE PROPERTY
    @property
    def size(self):
        """Returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
