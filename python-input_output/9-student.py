#!/usr/bin/python3
"""Making the student class"""


class Student:
    """Student"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """just like the simulations!"""
        return obj.__dict__
