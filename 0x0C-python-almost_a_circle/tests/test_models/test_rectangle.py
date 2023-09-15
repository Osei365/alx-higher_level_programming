#!/usr/bin/python3
"""Defines test cases for class Rectangle."""


import unittest
import sys
import io
from models.rectangle import Rectangle, Base


class TestRectangle(unittest.TestCase):
    """represents the test cases for rectangle class."""

    def setUp(self):
        """This is run before test cases"""
        self.r1 = Rectangle(3, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(8, 7, 0, 0, 12)
        self.r4 = Rectangle(2, 2)
        self.r5 = Rectangle(2, 3, 2, 2)
        self.r6 = Rectangle(10, 10, 10, 10)

    def test_init(self):
        """test cases for init (constructor) function"""

        self.assertEqual(self.r2.id, self.r1.id + 1)
        self.assertEqual(self.r1.id, self.r2.id - 1)
        self.assertEqual(self.r3.id, 12)

    def test_widthsetter(self):
        """test cases for Rectabgle setter methods"""
        with self.assertRaises(TypeError):
            self.r1.width = "2"
            self.r1.width = {"2", "e", "l"}
            self.r1.width = [1, 2, 3, ["my guy"]]
            self.r1.width = {}
            self.r1.width = [23, 45, 32]

        with self.assertRaises(ValueError):
            self.r1.width = 0
            self.r1.width = -4

    def test_heightsetter(self):
        """test cases for Rectabgle setter methods"""
        with self.assertRaises(TypeError):
            self.r1.height = "2"
            self.r1.height = {"2", "e", "l"}
            self.r1.height = [1, 2, 3, ["my guy"]]
            self.r1.height = {}
            self.r1.height = [23, 45, 32]

        with self.assertRaises(ValueError):
            self.r1.height = 0
            self.r1.height = -4

    def test_xsetter(self):
        """test cases for Rectabgle setter methods"""
        with self.assertRaises(TypeError):
            self.r1.x = "2"
            self.r1.x = {"2", "e", "l"}
            self.r1.x = [1, 2, 3, ["my guy"]]
            self.r1.x = {}
            self.r1.x = [23, 45, 32]

        with self.assertRaises(ValueError):
            self.r1.x = 0
            self.r1.x = -4

    def test_ysetter(self):
        """test cases for Rectabgle setter methods"""
        with self.assertRaises(TypeError):
            self.r1.y = "2"
            self.r1.y = {"2", "e", "l"}
            self.r1.y = [1, 2, 3, ["my guy"]]
            self.r1.y = {}
            self.r1.y = [23, 45, 32]

        with self.assertRaises(ValueError):
            self.r1.y = 0
            self.r1.y = -4

    def test_area(self):
        """test cases for area instance method."""
        self.assertEqual(self.r1.area(), 6)
        self.assertEqual(self.r2.area(), 20)
        self.assertEqual(self.r3.area(), 56)

    def cap_stdout(self, rect, isprint=False):
        """captures stdout"""
        capture = io.StringIO()
        sys.stdout = io.StringIO()
        if isprint:
            print(rect)
        else:
            rect.display()
        output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__

        return output

    def test_display(self):
        """test cases for display method in
        Rectangle."""
        self.assertEqual(self.cap_stdout(self.r4), "##\n##\n")
        self.assertEqual(self.cap_stdout(self.r1), "###\n###\n")
        result = "##\n##\n##\n##\n##\n##\n##\n##\n##\n##\n"
        self.assertEqual(self.cap_stdout(self.r2), result)
        result2 = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(self.cap_stdout(self.r5), result2)

    def test_str(self):
        """test cases for string representation"""
        case1 = f"[Rectangle] ({self.r1.id}) {self.r1.x}/{self.r1.y} \
- {self.r1.width}/{self.r1.height}\n"
        case2 = f"[Rectangle] ({self.r3.id}) {self.r3.x}/{self.r3.y} \
- {self.r3.width}/{self.r3.height}\n"
        case3 = f"[Rectangle] ({self.r5.id}) {self.r5.x}/{self.r5.y} \
- {self.r5.width}/{self.r5.height}\n"

        self.assertEqual(self.cap_stdout(self.r1, True), case1)
        self.assertEqual(self.cap_stdout(self.r3, True), case2)
        self.assertEqual(self.cap_stdout(self.r5, True), case3)

    def test_update(self):
        """test cases for update"""
        "updating nothing"
        self.r6.update()
        case0 = f"[Rectangle] ({self.r6.id}) 10/10 - 10/10\n"
        self.assertEqual(self.cap_stdout(self.r6, True), case0)
        "updating just one"
        self.r6.update(89)
        case1 = "[Rectangle] (89) 10/10 - 10/10\n"
        self.assertEqual(self.cap_stdout(self.r6, True), case1)
        "updating two args"
        self.r6.update(89, 2)
        case2 = "[Rectangle] (89) 10/10 - 2/10\n"
        self.assertEqual(self.cap_stdout(self.r6, True), case2)
        "updating three args"
        self.r6.update(89, 2, 3)
        case3 = "[Rectangle] (89) 10/10 - 2/3\n"
        self.assertEqual(self.cap_stdout(self.r6, True), case3)
        "updating four args"
        self.r6.update(89, 2, 3, 4)
        case4 = "[Rectangle] (89) 4/10 - 2/3\n"
        self.assertEqual(self.cap_stdout(self.r6, True), case4)
        "updating five args"
        self.r6.update(89, 2, 3, 4, 5)
        case5 = "[Rectangle] (89) 4/5 - 2/3\n"
        self.assertEqual(self.cap_stdout(self.r6, True), case5)

        """test cases for update with kwargs"""
        """with args and kwargs (kwargs are to beoverlooked when
        args exist and are not empty)"""
        self.r6.update(10, id=34)
        case7 = "[Rectangle] (10) 4/5 - 2/3\n"
        self.assertEqual(self.cap_stdout(self.r6, True), case7)
        "test kwargs insertions"
        self.r6.update(id=34, width=9, height=10, x=7, y=23)
        case8 = "[Rectangle] (34) 7/23 - 9/10\n"
        self.assertEqual(self.cap_stdout(self.r6, True), case8)

    def test_to_dictionary(self):
        """test cases for to_dictionary method"""
        r8_dict = Rectangle(10, 2, 1, 9).to_dictionary()
        keys = ["id", "width", "height", "x", "y"]
        self.assertEqual(type(r8_dict), dict)
        self.assertEqual(list(r8_dict.keys()), keys)
        self.assertEqual(r8_dict["width"], 10)
        self.assertEqual(r8_dict["height"], 2)
        self.assertEqual(r8_dict["x"], 1)
        self.assertEqual(r8_dict["y"], 9)
