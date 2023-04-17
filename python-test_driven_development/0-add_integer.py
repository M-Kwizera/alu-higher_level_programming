#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b


print(add_integer(1, 2.2))
