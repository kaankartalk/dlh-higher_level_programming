#!/usr/bin/python3
"""
This module cntains a function that writes a sting to a text file.
"""


def write_file(filename="", text=""):
    """a UTF-8 text file and return number of charcters."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
