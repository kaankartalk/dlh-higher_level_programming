#!/usr/bin/python3
"""
Serialization and filtering.
"""


class Student:
    """Defines first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return all attributes.
        """
        if isinstance(attrs, list) and all(type(a) is str for a in attrs):
            return {key: self.__dict__[key] for key in attrs if key in self.__dict__}
       return self.__dict__
