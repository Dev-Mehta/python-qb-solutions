"""
312 - Write a python program to create string out of first, middle and last character
"""

def createStr(string: str) -> str:
    # Return original string if length is less than 3
    # As we atleast need, more than 3 characters to pick up,
    # first, middle and last character from a string
    if len(string) <= 3:
        return string
    return string[0] + string[(len(string)-1)//2] + string[-1]

print(f"New string: {createStr(input('Enter a string: '))}")