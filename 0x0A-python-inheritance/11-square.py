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
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ string representation of the class Square"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
