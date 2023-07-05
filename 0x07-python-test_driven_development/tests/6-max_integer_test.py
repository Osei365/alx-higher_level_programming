#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Represents max integer test class."""

    def test_max_integer(self):
        """test all edge cases using max_integer function."""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2, 4, 6, 1, 3]), 6)
        self.assertEqual(max_integer([34, 68, 23]), 68)
        self.assertEqual(max_integer([9]), 9)
        self.assertEqual(max_integer([3.4, 3.5, 3.6, 3.1]), 3.6)
        self.assertEqual(max_integer([10, 9, 8, 7]), 10)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-3, 1, 3, 6, 9]), 9)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
