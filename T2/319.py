"""
319: Write a python program to create string made out of middle three characters
"""

def createStr(string: str) -> str:
    if len(string) <= 3:
        return string
    mid = (len(string)-1)//2
    return string[mid-1] + string[mid] + string[mid+1]

print(createStr(input("Enter a string: ")))