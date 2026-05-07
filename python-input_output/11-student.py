#!/usr/bin/python3
"""
Defines a Student class with JSON serialization/deserialization
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes are returned.
        """
        if isinstance(attrs, list) and all(type(a) is str for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        using the provided dictionary.
        """
        fr key, value in json.items():
            setattr(self, key, value)
