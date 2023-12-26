"""
307 - Write a python program to find number of uppercase and lowercase letters in string
"""

def findUpperLower(string: str) -> tuple:
    """
    Returns the number of uppercase and lowercase letters in string.
    Parameters:
        string (str): The input string that we will work on
    Returns:
        int: 2-valued tuple with t[0] being number of uppercase letters, and t[1] being number of lowercase letters
    """
    u, l = 0, 0
    for i in string:
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1
    return u, l

s = input("Enter a string: ")
u,l = findUpperLower(s)
output = f"Uppercase: {u}\nLowercase: {l}"
print(output)