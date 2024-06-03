#!/usr/bin/python3
"""class the defaine a Rectangle"""


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """instantiation"""
        if __check_value(width):
            self.width = width
        if __check_value(height):
            self.height = height

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__width

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __check_value(self, value):
        """check value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        return True

