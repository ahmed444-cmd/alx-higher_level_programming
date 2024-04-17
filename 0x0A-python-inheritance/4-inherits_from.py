#!/usr/bin/python3
"""Definition of  an inherit class-checking funct."""


def inherits_from(obj, a_class):
    """
        inherits_from returns true if object is instance of a class
        that inherited directly or indirectly from the specified class.
        Args:
            obj (object): object.
            a_class (class): class.
        Returns: True or False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
