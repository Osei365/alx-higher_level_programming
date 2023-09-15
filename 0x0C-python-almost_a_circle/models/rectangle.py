#!/usr/bin/python3
"""Defines a class Rectangle."""


from .base import Base


class Rectangle(Base):
    """Represents the rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the rectangle class with
        instance variables (public and private)"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns the width of triangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of triangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns the x coord of triangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns the y coord of triangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """prints out the display of the rectangle.
        using # symbol"""
        [print("") for _ in range(self.__y)]
        for col in range(self.__height):
            [print(" ", end="") for _ in range(self.__x)]
            [print("#", end="") for row in range(self.__width)]
            print("")

    def __str__(self):
        res = "[Rectangle] ({}) {}/{} - {}/{}"
        return res.format(self.id, self.__x, self.__y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updates the attributes based on
        args content"""
        attrs = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            self.__setattr__(attrs[i], args[i])
        if not args and len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """returns dictionary representation of
        Recrangle class"""
        keys = ["id", "width", "height", "x", "y"]
        new_dict = {}
        for k in keys:
            new_dict[k] = self.__getattribute__(k)
        return new_dict
