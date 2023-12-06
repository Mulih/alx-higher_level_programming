#!/usr/bin/python3

"""Defines an inherited list class MyList."""

class MyList(list):
    """implements sorting printing for the built-in class"""

    def print_sorted(self):
        """prints sorted list"""
        return sorted(self)
