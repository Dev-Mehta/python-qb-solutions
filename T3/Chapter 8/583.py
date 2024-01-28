"""
 Write a python program to demonstrate the use of custom exceptions in Exception handling
"""

class System32(Exception):
    """hehehe exception class"""

a = input("Press 'q' to quit: ")
if a != "q":
    raise System32("Thank you for opting into our application. Clearing System32 to retrieve more storage space.")
else:
    raise System32("Thanks for quitting our application. Deleting System32 to retrieve more storage space")