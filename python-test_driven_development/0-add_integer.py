#!/usr/bin/python3
# This function add_integer takes in two arguments and returns the sum of them
# def add_integer(a, b=98):
#     """
#     add_integer takes in two arguments
#     checks whether argument (a) and (b) are of integer type
#     if they are not integers raises TypError 'must be an integer' or 'b must be an integer'
#     Proceeds with casting a and b as integers
#     Returns a + b
#     """
#     if not isinstance(a, int):
#         raise TypeError("a must be an integer")
#     if not isinstance(b, int):
#         raise TypeError("b must be an integer")
#     a = int(a)
#     b = int(b)
#     return a + b

def add_integer(a, b=98):
    """ Should the conditions be met, Raising the type error message"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
