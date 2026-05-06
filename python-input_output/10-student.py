#!/usr/bin/python3
"""
Student class module
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return dictionary representation of the Student.
        If attrs is a list of strings, return only those attributes.
        """
        if isinstance(attrs, list) and all(type(a) is str for a in attrs):
            return {
                key: self.__dict__[key]
                for key in attrs
                if key in self.__dict__
            }
        return self.__dict__
