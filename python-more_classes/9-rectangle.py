#!/usr/bin/python3
"""
Docstring for the Rectangle class
"""


class Rectangle:
    """The Rectangle class with width and height properties"""
    #  Instances and string representation
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def print(self):
        """Prints the rectangle"""
        if self.height == 0 or self.width == 0:
            return
        for i in range(self.height):
            print(str(self.print_symbol) * self.width)

    def __str__(self):
        """Prints all the invisible text too so you can see what's
        happening under the hood"""
        if self.height == 0 or self.width == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.width
                         for _ in range(self.height))

    def __repr__(self):
        """Returns the copy/paste version of the function
        if you want to recerate it"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints out a goodbye before deleting the object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = Rectangle.area(rect_1)
        area2 = Rectangle.area(rect_2)
        if area1 > area2 or area1 == area2:
            return rect_1
        else:
            return rect_2

class Square(Rectangle, size="0"):
    def __init__(self):
        size = size
        super().__init__ = (size, size)
        return self
