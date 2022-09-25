#!/usr/bin/python3

""" Inherit from int """


class MyInt(int):
    """ subclass myInt from int class """
    def __eq__(self):
        """ return the not equal method instead"""
        return self.__ne__()

    def __ne__(self):
        """ return True if equal values"""
        return self.__eq__()
