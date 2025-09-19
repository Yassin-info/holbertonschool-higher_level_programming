#!/usr/bin/python3
"""Module 3-rectangle
Defines a Rectangle class with width, height, area, perimeter,
and string representation.
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

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """
        Return the string representation of the rectangle using the '#'
        character.

        This method constructs a visual representation of the rectangle by
        generating a string consisting of lines of '#' characters. The number
        of lines corresponds to the rectangle's height, and each line contains
        '#' repeated according to the rectangle's width.

        If either the width or height of the rectangle is 0, an empty
        string is returned.
        Returns:
            str: A string representing the rectangle with '#' characters,
            or an
                empty string if width or height is 0.
        Example:
            For a rectangle with width=4 and height=3, this method returns:
            ####
            ####
            ####
        """
        if (self.width == 0) or (self.height == 0):
            return ""
        lines = []
        for i in range(self.height):
            lines.append("#" * self.width)
        return "\n".join(lines)

    def __repr__(self):
        """
        Return a string representation of the rectangle for eval().

        Returns:
            str: String that can recreate the instance.
        """
        return f"Rectangle({self.__width}, {self.__height})"
