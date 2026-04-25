#!/usr/bin/python3
from calculator_1 import add, sub

def magic_calculation(a, b):
    if a < b:
        return add(a, b)
    else:
        return sub(a, b)
