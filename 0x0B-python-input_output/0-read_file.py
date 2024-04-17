#!/usr/bin/python3

"""Definition of  a text file-reading funct."""


def read_file(filename=""):
    """Contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
