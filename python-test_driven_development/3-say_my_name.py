#!/usr/bin/python3

"""This module contains a function
    'say_my_name '"""


def say_my_name(first_name, last_name):
    """Checking if first_name and last_name
        are strings."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name is None:
        raise TypeError(
            "Traceback (most recent call last):\n...\nTypeError: say_my_name() missing 1 required positional argument: 'first_name'")
    print(F"My name is {first_name} {last_name}")
