#!/usr/bin/python3
"""Module contains print_square"""


def print_square(size):
    """" this function Prints a square
    based on the size provided. """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
