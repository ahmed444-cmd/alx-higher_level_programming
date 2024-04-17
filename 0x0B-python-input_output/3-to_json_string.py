#!/usr/bin/python3

"""Definition of a string-to-JSON func."""
import json


def to_json_string(my_obj):
    """Return the JSON rep of a string objct."""
    return json.dumps(my_obj)
