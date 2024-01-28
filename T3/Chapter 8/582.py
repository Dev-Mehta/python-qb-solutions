"""
Write a python program to demonstrate the 
use of raise in Exception handling
"""

a = input("Enter a number: ")
if len(a) != 10:
    raise ValueError("Kidhu ne number nakhvanu")
print("Kidhu number nakhvanu etle nakhi devano?")