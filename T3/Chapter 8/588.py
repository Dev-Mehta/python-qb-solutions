"""
Write a python program that has a class Point with attributes as the x and y co-ordinates. 
1.	Add a method ‘distance from origin’ to class Point which returns the distance of the given point from origin. The equation 
is 
2.	Add a method ‘translate’ to class Point, which returns a new position of point after translation
3.	Add a method ‘reflect_x’ to class Point, which returns a new point which is the reflection of the point about the x-axis. 
4.	Add a method ‘distance’ to return distance of the given point with respect to the other point. The formula for calculating 
distance between A(x1,y1) and B(x2,y2) is 
After creating class blueprint run the following test case - 
Test Case – Point (1,2)
Distance from origin - 2.23
Translate method - point (1,2) translated by (1,1) increment will be at (2,3) now
Reflect_x Method - Point (2,3) after given reflection will be at (2,-3)
Distance Method - distance between point (2,-3) and (3,4) is 1.41
"""
import math

class Point:
    def __init__(self,x:int,y: int):
        self.x = x
        self.y = y

    def translate(self,x:int,y:int):
        return Point(self.x+x, self.y+y)

    def distance_from_origin(self):
        return self.distance(0,0)

    def reflect_x(self):
        # (test case states 2,3 to 2,-3)
        # mathematically it should be 2,3 to -2, 3 
        # as we are changing x but not y but whatever. All hail the QB
        return Point(self.x, -self.y)

    def distance(self, x2, y2):
        return round(math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2),2)
    
    def __str__(self) -> str:
        return self.__class__.__name__ + '(' + str(self.x) + ',' + str(self.y) + ')'
p = Point(1,2)
print(p.distance_from_origin())
p = p.translate(1,1)
print(p)
p = p.reflect_x()
print(p)
print(p.distance(3,4))
