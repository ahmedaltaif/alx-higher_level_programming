#!/usr/bin/python3
"""empty class Square with size"""


class Square:
    """with privat size attribute"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be an intege')
        self.__size = size

