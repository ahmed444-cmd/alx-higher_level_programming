#!/usr/bin/python3

"""Definition of an inherited lst clss MyList."""


class MyList(list):
    """sorted printing for the built-in lst clss."""

    def print_sorted(self):
        """Prints a lst in ascending order."""
        print(sorted(self))
