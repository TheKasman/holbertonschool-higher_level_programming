#!/usr/bin/python3
"""This module defines the Square class again.. again?"""


class Square:
    """The Square class NOW WITH DEFINED SIZE"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor for a new square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

    def area(self):
        """Calculates and returns the current area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using #"""
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
        
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

    # POSITION PROPERTY
    @property
    def position(self):
        """Returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(x, int) for x in value) or
            not all(x >= 0 for x in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
