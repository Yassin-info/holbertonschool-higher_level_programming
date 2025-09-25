#!/usr/bin/env python3
"""
This module defines an abstract base class Animal using Python's abc module.
It also implements two concrete subclasses: Dog and Cat.

Classes:
    Animal -- Abstract base class with an abstract method sound()
    Dog -- Subclass of Animal, implements sound() to return "Bark"
    Cat -- Subclass of Animal, implements sound() to return "Meow"
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Abstract method that should be implemented
        by all Animal subclasses"""
        pass


class Dog(Animal):
    def sound(self):
        """Return the sound made by a dog"""
        return "Bark"


class Cat(Animal):
    def sound(self):
        """Return the sound made by a cat"""
        return "Meow"
