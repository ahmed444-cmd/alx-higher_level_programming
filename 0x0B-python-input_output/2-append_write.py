#!/usr/bin/python3

"""Definition of a file-appending function."""


def append_write(filename="", text=""):
    """String to the end of a UTF8 text file.
    Args:
        filename (str): The name of the file.
        text (str): The string text.
    Returns:
        The numb of chars appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
