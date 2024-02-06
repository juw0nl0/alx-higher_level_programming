#!/usr/bin/python3
"""a function that returns True if the object is exactly
an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """Returns True if obj is same instance, else False
    """

    if type(obj) is a_class:
        return True
    else:
        return False
