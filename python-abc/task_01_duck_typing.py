#!/usr/bin/python3

"""Abstract classes task 0"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape Abstract class"""
    @abstractmethod
    def area(self):
        """Area Method"""
        pass

    @abstractmethod
    def perimeter(self):
        """the perimeter method"""
        pass


class Circle(Shape):
    """Circle class"""
    def __init__(self, radius):
        """constructor"""
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be an number")
        if radius <= 0:
            raise ValueError("radius must be > 0")
        self.radius = radius

    def area(self):
        """Returns the area as pi r squared"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """you guessed it, returns 2 pi r"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""
    def __init__(self, width, height):
        """constructor"""
        if not isinstance(width, (int, float)):
            raise TypeError("width must be an number")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be an number")
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be > 0")

        self.width = width
        self.height = height

    def area(self):
        """Much easier. returns xy"""
        return self.height * self.width

    def perimeter(self):
        """returns 2(x + y)"""
        return 2 * (self.width + self.height)
