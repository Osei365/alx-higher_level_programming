#!/usr/bin/python3
"""Defines test cases for class Base."""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """represents the test cases for base class."""

    def setUp(self):
        """This is run before test cases"""
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

    def test_init(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)
