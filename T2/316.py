"""
316 - Write a program to print even length words in a string
"""

def printEven(string: str) -> None:
    string = string.split()
    for i in string:
        if len(i) % 2 == 0:
            print(i)
    # I/P: Python is somehow an easy lang
    # O/P:
    #   Python
    #   is 
    #   an
    #   easy
    #   lang
    # somehow = 7(odd) won't be printed
    # thala for a reason :)
printEven(input("Enter a string: "))