"""
Write a Python class named Student with two 
attributes student_name, marks. Modify the attribute 
values of the said class and print the original and 
modified values of the said attributes
"""

class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks
    def print(self):
        print("Name: " + self.student_name)
        print(f"Marks: {self.marks}")
s = Student("Dev", 20)
print("Original: ")
s.print()
s.student_name = "Stavan"
s.marks = 22
print("\nModified")
s.print()