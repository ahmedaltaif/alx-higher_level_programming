#!/usr/bin/python3
def add_integer(a, b=98):
    """add tow num"""
    if a is not int or float:
        raise TypeError('a must be an integer')
    if b is not int or float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)

    