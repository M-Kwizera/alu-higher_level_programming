#!/usr/bin/python3
"""Module contains print_square"""


def print_square(size):
    """Function prints a square
    based on the size specified."""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be an integer")
    if isinstance(size, float) < 0:
        raise TypeError("size must be an integer")

    # num = int(input("Enter number: "))
    for i in range(size):
        print("#"*size)
