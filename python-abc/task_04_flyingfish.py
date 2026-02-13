#!/usr/bin/python3

"""Flying fish module"""

class Bird:
    """dad there's a bird in the house! WHAT DO YOU MEAN A BIRD!?"""
    def fly(self):
        """I believe i can flyyy"""
        print("The bird is flying")
    
    def habitat(self):
        """habitat method"""
        print("The bird lives in the sky")  

class Fish:
    """Today's fish is trout al a creme. Enjoy your meal"""
    def swim(self):
        """swim"""
        print("The fish is swimming")
    def habitat(self):
        """habitat"""
        print("The fish lives in the water")

class FlyingFish(Fish, Bird):
    def fly(self):
        """Fly!"""
        print("The flying fish is soaring!")
    
    def swim(self):
        """Swim!"""
        print("The flying fish is swimming!")
    
    def habitat(self):
        """in it's natural habitat"""
        print("The flying fish lives both in water and the sky!")
