"""
325 - Write a python function to shift decimal digits n places to left
"""

def shiftN(string: str, shift: int) -> str:
    return string[shift:] + string[:shift]

s = input("Enter a string: ")
shift = int(input("Enter shift: "))
print(shiftN(s, shift))