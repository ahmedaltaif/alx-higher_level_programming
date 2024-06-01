#!/usr/bin/python3
"""empty class Square with size"""


class Square:
    """with privat size attribute"""
    def __init__(self, size=0):
        """The __init__ method initializes the size value of the square."""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    def area(self):
        """return the area"""
        return self.__size * self.__size
