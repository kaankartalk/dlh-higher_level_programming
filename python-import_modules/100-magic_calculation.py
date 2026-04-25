#!/usr/bin/python3
from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                result = add(result, i)
            else:
                result = sub(result, i)
        except Exception:
            result = add(result, b)
            break
    return result
