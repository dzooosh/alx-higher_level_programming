#!/usr/bin/python3

""" Inherit from int """


class MyInt(int):
    """ subclass myInt from int class """
    def __eq__(self):
        """ return the not equal method instead"""
        s = super.__ne__()
        return s

    def __ne__(self):
        """ return True if equal values"""
        s = super().__eq__()
        return s
