"""
326: Write a program to count all uppercase, lowercase, 
and number of digits in a string
"""

def calculate(string: str) -> (int, int, int):
    u, l, d = 0,0,0
    for i in string:
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1
        elif i.isdigit():
            d += 1
    return u, l, d

u, l, d = calculate(input("Enter a string: "))
print(f"Uppercase: {u}, Lowercase: {l}, Digits: {d}")