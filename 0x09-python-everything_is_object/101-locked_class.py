#!/usr/bin/python3
"""definition of LockedClass."""


class LockedClass:
    """
    Prevent the user from new LockedClass attributes
    for anything except attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
