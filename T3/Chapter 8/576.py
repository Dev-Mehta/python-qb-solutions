"""
Write a Python program to create a Vehicle class 
with max_speed and mileage instance attributes
"""

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage =mileage

car = Vehicle(180,20)
print(f"Car's max speed is {car.max_speed}, and has {car.mileage} mileage.")