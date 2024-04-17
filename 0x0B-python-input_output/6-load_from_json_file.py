#!/usr/bin/python3
"""
    Defines load_from_json_file()
"""


import json


def load_from_json_file(filename):
    """
        loads an objct to from JSON file.
        Args:
            filename (str): file name.
    """
    with open(filename, "r") as j_file:
        my_obj = json.load(j_file)
        return my_obj
