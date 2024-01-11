"""
308 - Write a python program to find length of a string in python without using len()
"""

def findLen(string: str) -> int:
    """
    Returns the length of string.
    Parameters:
        string (str): The string whose length we need to find
    Returns:
        int: Length of string
    """
    # return len(string)
    # if question explicitly asks to not use len()
    str_len = 0
    for i in string:
        str_len += 1
    return str_len

s = input("Enter a string: ")
output = f"Length of given string is {len(s)}"
print(output)