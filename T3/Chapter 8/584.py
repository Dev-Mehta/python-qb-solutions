"""
Write a program to build a simple Student Management System using Object Oriented Programming in 
Python which can perform the following operations:

accept-This method takes details from the user like name, 
roll number, and marks for two different subjects. 

display-This method displays the details of every student.

search-This method searches for a particular student from 
the list of students. This method will ask the user for roll 
number and then search according to the roll number

delete-This method deletes the record of a particular 
student with a matching roll number.

update-This method updates the roll number of the student. This 
method will ask for the old roll number and new roll number. It will replace the 
old roll number with a new roll number.

The following instructions need to be considered while making a program.
1.	Give class name as Student
2.	Include methods name as accept, display, 
    search, delete and update. 
    (1 mark for each correct method to be formed).
3.	Also form constructor with __init__ () 
    method (2 marks for forming constructor).
4.	2 marks for correct object prepared like 
    after deletion of one roll no of student 
    it should update the list with new roll no. 
    and should display it.

The example is just for understanding but logic 
should be for any n number of students.

For Example:

List of Students
Name : A
RollNo : 1
Marks1 : 100
Marks2 : 100
Name : B
RollNo : 2
Marks1 : 90
Marks2 : 90
Name : C
RollNo : 3
Marks1 : 80
Marks2 : 80
Student Found,
Name : B
RollNo : 2
Marks1 : 90
Marks2 : 90
List after deletion
Name : A
RollNo : 1
Marks1 : 100
Marks2 : 100
Name : C
RollNo : 3
Marks1 : 80
Marks2 : 80
List after updation
Name : A
RollNo : 1
Marks1 : 100
Marks2 : 100
Name : C
RollNo : 2
Marks1 : 80

"""

class Student:
    # I have used dictionary instead of list
    # because dictionary completes operation in constant time
    # compared to lists where search operation takes O(n) time
    students = {}
    def __init__(self, name: str, roll_no: int, marks: list):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        Student.students.update({self.roll_no: self})

    def accept(self):
        name = input("Enter name: ")
        roll_no = int(input("Enter roll no: "))
        while roll_no in Student.students.keys():
            print("Student with that roll_no is already existing. Assign another number to")
            roll_no = int(input("Enter roll_no: "))
        marks = eval(input("Enter marks in list: "))
        while type(marks) != list:
            marks = eval(input("Enter marks in list: "))
        Student(name, roll_no, marks)
        print("Student accepted successfully")
    
    def __str__(self) -> str:
        return f"Name: {self.name}, Roll no: {self.roll_no}, Marks: {self.marks}"

    def display(self):
        for i in Student.students.values():
            print(i)
        
    def search(self):
        roll_no = int(input("Enter roll number to search: "))
        s = Student.students.get(roll_no, None)
        if s == None:
            print("Student not found in records.")
        else:
            print("Student found")
            print("Student name: " , s.name)
            print("Student roll number: " , s.roll_no)
            print("Student marks: ", s.marks)
        
    def delete(self):
        roll_no = int(input("Enter roll number to delete: "))
        s = Student.students.get(roll_no, None)
        if s is not None:
            del Student.students[roll_no]
        else:
            print("Student roll number not found. Can't delete non existing student")

    def update(self):
        roll_no = int(input("Enter roll number to update: "))
        s = Student.students.get(roll_no, None)
        if s is not None:
            c = Student(s.name, s.roll_no, s.marks)
            c.roll_no = int(input("Enter new roll number: "))
            del Student.students[roll_no]
            Student.students.update({c.roll_no:c})
        else:
            print("Student not found with roll number.")

student_system = Student("Dev", 1, [23,22])
student_system.accept()
student_system.accept()
student_system.accept()
student_system.display()
student_system.search()
student_system.delete()
student_system.display()
student_system.update()
student_system.display()