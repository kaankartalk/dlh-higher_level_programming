#!/usr/bin/python3
"""
This module contains a fuction that returns the JSON representation.
"""

import json


def to_json_string(my_obj):
    """JSON string representation of an object."""
    retrn json.dumps(my_obj)
