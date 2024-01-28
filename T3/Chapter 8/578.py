"""
Write a Python class named Student with two 
attributes student_id, student_name. Add a new attribute 
student_class. Create a function to display the entire 
attribute and their values in Student class.
"""

class Student:
    def __init__(self, student_id, student_name, student_class=None):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display(self):
        print("Student id: ", self.student_id)
        print("Student name: ", self.student_name)
        print("Student class: ", self.student_class)

s = Student(1,"Dev")
s.display()
s = Student(2, "Stavan", "D1")
s.display()