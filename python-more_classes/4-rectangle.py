#!/usr/bin/python3
"""
Docstring for the Rectangle class
"""


class Rectangle:
    """The Rectangle class with width and height properties"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle - with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle - with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the preimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def print(self):
        """Prints the rectangle"""
        if self.height == 0 or self.width == 0:
            return ""
        for i in range(self.height):
            if i < self.height - 1:
                print("#" * self.width)
            else:
                print("#" * self.width, end="")

    def __str__(self):
        """Prints all the invisible text too so you can see what's
        happening under the hood"""
        if self.height == 0 or self.width == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))

    def __repr__(self):
        """Returns the copy/paste version of the function
        if you want to recerate it"""
        return f"Rectangle({self.width},{self.height})"
