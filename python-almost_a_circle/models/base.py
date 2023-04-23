#!/usr/bin/python3
"""Module with ..."""


class Base:

    """Class Base is a basic
    representation of what a
    simple python3 class looks
    like"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
