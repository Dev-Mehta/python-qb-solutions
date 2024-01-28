"""
Write a Python class named Circle constructed by a radius 
and two methods which will compute the area and the perimeter 
of a circle.
"""

import math

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def circumference(self):
        return 2 * self.radius * math.pi
    
    def area(self):
        return self.radius**2 * math.pi
    
    def display(self):
        print("Radius: ", self.radius)
        print("Area: ", self.area())
        print("Perimeter: ", self.circumference())

c = Circle() # will take 1 as default radius
c.display()