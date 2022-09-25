#!/usr/bin/python3

"""Square class that inherit from rectangle base class"""
Rectangle = __import__('9-rectangle').Square

class Square(Rectangle):
    """ subclass square """
    def __init__(self, size):
        """ Initialization of class square

        Args:
            size: size of the square (private)
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area of the square """
        return self.__size * self.__size

    def __str__(self):
        """ string representation of the class Square"""
        string = "[" + self.__class__.__name__ + "] "
        string += "<" + self.__width + ">/<" + self.__height + ">"
        return string
