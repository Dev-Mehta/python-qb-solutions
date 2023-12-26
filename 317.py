"""
317: Write a python program to print uppercase half string
"""

def createStr(string: str) -> str:
    firsthalf = string[:len(string-1)//2]
    secondhalf = string[len(string-1)//2:]
    firsthalf = firsthalf.upper()
    secondhalf = secondhalf.lower()
    return firsthalf + secondhalf

print(createStr(input("Enter a string: ")))