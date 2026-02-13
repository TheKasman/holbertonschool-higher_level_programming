#!/usr/bin/python3

"""Abstract classes task 0"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Animal Abstract class"""
    @abstractmethod
    def sound(self):
        """A sound for an animal to say"""
        pass  

class Dog(Animal):
    """Doge class"""

    def sound(self):
        """Woofers go woof"""
        return "Bark"
    
class Cat(Animal):
    """kore nani? NEKOO"""
    def sound(self):
        return "Meow"