"""
311 - Write a python program to remove i-th character from string
"""

def remove(string: str, index: int) -> str|None:
    if index < 0 or index >= len(string):
        return None
    string = string[:index] + string[index+1:]
    return string

s = input("Enter a string: ")
index = int(input("Enter the index: "))
print(f"Before removing character @ {index} index: {s}")
s = remove(s, index)
print(f"After removing @ {index} index: {s}")