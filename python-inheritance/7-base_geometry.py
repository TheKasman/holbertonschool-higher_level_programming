#!/usr/bin/python3

"""Base Geometry functions/classes coming in"""


class BaseGeometry():
    """Base Geometry"""
    def area(self):
        """returns the area of the geometric shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that an integer is being parsed"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
