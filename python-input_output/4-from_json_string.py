#!/usr/bin/python3
"""
JSON string to a Python object.
"""

import json


def from_json_string(my_str):
    """Return the Python objct a JSON string."""
    return json.loads(my_str)
