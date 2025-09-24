#!/usr/bin/python3
"""Module that defines a Rectangle class with area and string
representation."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Placeholder method for area computation."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a strictly positive integer.

        Args:
            name (str): the name of the value (for the error message)
            value (int): the value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""
    def __init__(self, width, height):
        """Initialize a Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Placeholder method for area computation."""
        return (self.__height * self.__width)

    def __str__(self):
        """Return the string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
