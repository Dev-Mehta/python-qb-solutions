"""
Write a Python Program to Find the Net Salary of Employee using Inheritance.
Create three Class Employee, Perks, NetSalary. Make an Employee class as an abstract class.
Employee class should have methods for following tasks.
- To get employee details like employee id, name and salary from user.
- To print the Employee details.
- return Salary.
- An abstract method emp_id.
Perks class should have methods for following tasks.
- To calculate DA, HRA, PF.
- To print the individual and total of Perks (DA+HRA-PF).
Netsalary class should have methods for following tasks.
- Calculate the total Salary after Perks.
- Print employee detail also prints DA, HRA, PF and net salary.
Note 1: DA-35%, HRA-17%, PF-12%
Note 2: It is compulsory to create objects and demonstrating the methods with
Correct output. 
Example:
Employee ID: 1
Employee Name: John
Employee Basic Salary: 25000
DA: 8750.0
HRA: 4250.0
PF: 3000.0
Total Salary: 35000.0
"""
from abc import ABC, abstractmethod
class Employee(ABC):
    def get_emp_details(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    @abstractmethod
    def emp_id(self):
        pass
    def get_salary(self):
        return self.salary
class Perks(Employee):
    def calc_perks(self):
        self.da = self.salary*0.35
        self.hra = self.salary*0.17
        self.pf = self.salary*0.12
    def emp_id(self):
        return self.id
    def print(self):
        s = f"""Name: {self.name}
Id: {self.id}
Salary: {self.salary}
DA: {self.da}
HRA: {self.hra}
PF: {self.pf}"""
        print(s)
class NetSalary(Perks):
    def calc_salary(self):
        self.calc_perks()
        self.ns = self.salary + self.da + self.hra - self.pf
    def net_salary(self):
        return self.ns
    def emp_id(self):
        return self.id
n = NetSalary()
n.get_emp_details(1, "John", 25000)
n.calc_perks()
n.print()
n.calc_salary()
print("Net salary: ", n.net_salary())