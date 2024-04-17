#!/usr/bin/python3

"""Definition of a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Returns the Python object of a JSON string."""
    return json.loads(my_str)

