#!/usr/bin/python3
"""empty class Square with size"""


class Square:
    """with privat size attribute"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """getter func"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter func"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """return the area"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for x in range(self.__size):
                    print("#", end="")
                print()
