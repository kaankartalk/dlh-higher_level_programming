#!/usr/bin/python3
"""
for JSON serialization.
"""


def class_to_json(obj):
    """Return the dictionary representation of an object's attributes."""
    return obj.__dict__
