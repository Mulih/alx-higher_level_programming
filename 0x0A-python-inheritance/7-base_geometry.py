#!/usr/bin/python3

"""Defines a classs BaseGeometry."""

class BaseGeometry:
    """Represent base geometry."""
   
   def area(self):
       """Not implemented."""
       raise Exception("area() is not implemented")

   def integer_validator(self, name, value):
       """valida a parameter as an integer.

       Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate
       Raises:
            TypeError: If value is not an integer.
            ValueError: If value= 0.
       """
       if type(value) != int:
           raise TypeError("<name> must be an integer")
       if value <= 0:
       raise ValueError("<name> must be greater than 0")
       
