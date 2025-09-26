#!/usr/bin/env python3
"""
This module demonstrates multiple inheritance using a FlyingFish class
that inherits from both Fish and Bird. It overrides their methods to
demonstrate method resolution order (MRO).
"""


class Fish:
    """Represents a fish with swimming behavior and aquatic habitat."""

    def swim(self):
        """Print a message indicating the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """Represents a bird with flying behavior and aerial habitat."""

    def fly(self):
        """Print a message indicating the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print the habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A FlyingFish can both swim and fly.
    It overrides methods from both Fish and Bird.
    """

    def fly(self):
        """Print a message indicating the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print a message indicating the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
