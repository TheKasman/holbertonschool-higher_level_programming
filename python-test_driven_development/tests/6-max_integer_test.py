#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    #  Empty list
    def test_empty(self):
        self.assertIsNone(max_integer([]))

    #  One element
    def test_single(self):
        self.assertEqual(max_integer([5]), 5)

    #  Testing max int is registered from the back, front and middle
    def test_multiple(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    #  Negative numbers: Sprinkled in and all negative numbers
    def test_negative(self):
        self.assertEqual(max_integer([1, -2, 5, -6]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    #  Floats: both positive and negative
    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 70.125, 3.456]), 70.125)
        self.assertEqual(max_integer([-1.45, 2.4, -6]), 2.4)
