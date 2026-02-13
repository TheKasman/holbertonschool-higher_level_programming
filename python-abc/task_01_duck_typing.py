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
        self.width = width
        self.height = height

    def area(self):
        """Much easier. returns xy"""
        return self.height * self.width

    def perimeter(self):
        """returns 2(x + y)"""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Prints out information"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
