#!/usr/bin/python3

""" Inherit from int """


class MyInt(int):
    """ subclass myInt from int class """
    
    def __init__(self, value):
        """ initialization of class
        Args:
            value: the input number"""
        super().__init__(value)
        self.value = value

    def __eq__(self, other):
        """ return the not equal method instead"""
        return self.value != other.value

    def __ne__(self, other):
        """ return True if equal values"""
        return self.value == other.value
