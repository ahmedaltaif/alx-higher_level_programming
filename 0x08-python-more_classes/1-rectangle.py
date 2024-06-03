#!/usr/bin/python3
"""class the defaine a Rectangle"""


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """instantiation"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """getter"""
        return self.__width

    @width.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
