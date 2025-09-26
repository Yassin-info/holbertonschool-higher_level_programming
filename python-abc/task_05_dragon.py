#!/usr/bin/env python3
"""
This module demonstrates the use of mixins to compose behaviors.
It defines a Dragon class that can both
swim and fly using modular mixin classes.
"""


class SwimMixin:
    """Provides swimming ability to a class."""

    def swim(self):
        """Print a message indicating the creature can swim."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying ability to a class."""

    def fly(self):
        """Print a message indicating the creature can fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A mythical creature that can both swim and fly,
    composed using mixins for modular behaviors.
    """

    def roar(self):
        """Print a message indicating the dragon is roaring."""
        print("The dragon roars!")
