#!/usr/bin/python

"""The data turned into a pickle"""
import pickle


class MyObject:
    """MyObject class"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """It was then called... pickle rick"""
        with open(filename, "wb", encoding="utf-8") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """unpickle the pickle"""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (pickle.UnpicklingError, AttributeError,
                EOFError, ModuleNotFoundError):
            return None
