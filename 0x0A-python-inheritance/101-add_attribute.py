#!/usr/bin/python3


def add_attribute(clas, atr_name, inpt):
    """ add attribute to any class
    Args:
        clas: The class which to add attributes
        atr_name: The attribute name
        inpt: the inputed data for the attribute
    """
    if !(inspect.isclass(clas)):
        raise Exception("can't add new attribute")
    clas.atr_name = inpt
