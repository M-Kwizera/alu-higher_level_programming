#!/usr/bin/python3

"""This module contains a function 
    'say_my_name '"""


def say_my_name(first_name, last_name):
    """Checking if first_name and last_name
        are strings."""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    calling = (F"My name is {first_name} {last_name}")
    return calling


print(say_my_name("John", "Smith"))
