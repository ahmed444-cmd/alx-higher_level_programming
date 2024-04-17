#!/usr/bin/python3

"""Definition of a clss-check funct."""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a given clss.
    Args:
        obj: The object.
        a_class: The class to match.
    Returns:
        If obj is exactly an inst of a_clss - True.
        Else - False.
    """
    if type(obj) == a_class:
        return True
    return False
