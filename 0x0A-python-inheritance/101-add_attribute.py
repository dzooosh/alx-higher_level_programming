#!/usr/bin/python3


def add_attribute(clas, atr_name, inpt):
    """ add attribute to any class
    Args:
        clas: The class which to add attributes
        atr_name: The attribute name
        inpt: the inputed data for the attribute
    """
    if !(inspect.isclass(clas)):
        raise TypeError("can't add new attribute")
    else:
        setattr(clas, atr_name, inpt)
