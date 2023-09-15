#!/usr/bin/python3
"""defines a Square class that inherits
from a Rectangle class"""


from .rectangle import Rectangle


class Square(Rectangle):
    """represents the Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the square function."""

        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """gets the size attrib"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """representation when print to stdout"""
        string = "[Square] ({}) {}/{} - {}"
        return string.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """updates the attributes based on
        args content"""
        attrs = ["id", "size", "x", "y"]
        for i in range(len(args)):
            self.__setattr__(attrs[i], args[i])
        if not args and len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """returns dictionary representation of
        Recrangle class"""
        keys = ["id", "size", "x", "y"]
        new_dict = {}
        for k in keys:
            new_dict[k] = self.__getattribute__(k)
        return new_dict
