"""
Same as 320
331 - Write a python program to check if 2 strings are balanced
"""

"""
Two strings are balanced if
all characters of s1 are present in s2
"""
def isBalanced(s1: str, s2: str) -> bool:
    for i in s1:
        if i not in s2:
            return False
    return True

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
output = "Balanced" if isBalanced(s1,s2) else "Not balanced"
print(output)