#!/usr/bin/python3

"""Write a class Rectangle that inherits from BaseGeometry

    Instantiation with width and height: def __init__(self, width, height):
    width and height must be private. No getter or setter
    width and height must be positive integers, validated by integer_validator
    the area() method must be implemented
    print() should print, and str() should return,
    the following rectangle description: [Rectangle] <width>/<height>
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle Class inheriting from BaseGeometry.
    """
    def __init__(self, width, height):
        """Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the geometry"""
        return self.__width * self.__height

    def __str__(self):
        """Prints the area in a nice format"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
