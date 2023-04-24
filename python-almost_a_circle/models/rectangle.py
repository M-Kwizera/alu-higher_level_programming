#!/usr/bin/python3
from models.base import Base

"""Rectangle inherits from Base"""

# Base = __import__("base").Base


class Rectangle(Base):

    """Class Rectangle inherits from class base
    that is in the same directory(base.py)."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, a):
        """Width setter"""
        if type(a) != int:
            raise TypeError("width must be an integer")
        if a <= 0:
            raise ValueError("width must be > 0")
        self.__width = a

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, a):
        """set height"""
        if type(a) != int:
            raise TypeError("height must be an integer")
        if a <= 0:
            raise ValueError("height must be > 0")
        self.__height = a
