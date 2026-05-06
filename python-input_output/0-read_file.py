#!/usr/bin/python3
"""
This module contans a function that reads a text file and prints its content.
"""


def read_file(filename=""):
    """Read a UTF-8 text file and prnt its contents to stdou/."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
