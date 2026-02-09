#!/usr/bin/python3

"""Class and functions for MyList"""


class MyList(list):
    """MyList object does not need to initialise list"""
    def print_sorted(self):
        """Docstring for print_sorted
        :param self: Description
        """
        print(sorted(self))
