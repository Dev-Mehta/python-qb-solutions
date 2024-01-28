"""
Write a python program to demonstrate the 
use of try-except-else in Exception handling"""

try:
    a = {"name":"Dev"}
    print("Age", a['age'])
except Exception as e:
    print(e)
else:
    print("No exception occured")