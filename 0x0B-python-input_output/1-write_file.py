#!/usr/bin/python3

"""Definition of a file-writing function."""


def write_file(filename="", text=""):
    """prints a string to a UTF8 text file.
    Args:
        filename (str): The name of the file.
        text (str): The text to write on file.
    Returns:
        The numb of chars written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
