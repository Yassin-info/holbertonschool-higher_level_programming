#!/usr/bin/python3
"""
Module containing the Rectangle class.

This module defines a Rectangle class that inherits from BaseGeometry
and represents a rectangle with validated width and height.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    
    This class represents a rectangle with private width and height
    attributes that are validated to ensure they are positive integers.
    """
    
    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height.
        
        Both width and height are validated using the integer_validator
        method inherited from BaseGeometry to ensure they are positive
        integers.
        
        Args:
            width (int): The width of the rectangle (must be positive integer)
            height (int): The height of the rectangle (must be positive integer)
            
        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is less than or equal to 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
        self.__width = width
        self.__height = height
