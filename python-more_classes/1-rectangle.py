#!/usr/bin/python3
"""Module 1-rectangle
Defines a Rectangle class with width and height validation.
"""


class Rectangle:
    """
    Defines a rectangle with private width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.

        Args:
            width (int): Width of the rectangle (default 0).
            height (int): Height of the rectangle (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): New width.

        Raises:
            TypeError: If not an integer.
            ValueError: If less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): New height.

        Raises:
            TypeError: If not an integer.
            ValueError: If less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
