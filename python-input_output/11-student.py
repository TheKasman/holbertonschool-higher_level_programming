#!/usr/bin/python3
"""Making the student class - extended"""


class Student:
    """Student"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """just like the simulations!"""
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value
                    in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
