#!/usr/bin/python3

"""Definition of  an inherit class-checking funct."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.
    Args:
        obj : The object.
        a_class (type): The class to match.
    Returns:
        If obj is an inherited instance of a_class - True.
        Else - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
