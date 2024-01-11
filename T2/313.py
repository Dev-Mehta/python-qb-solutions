"""
313 - Write a python program to find all occurences of substring, ignore case.
"""

def countSubstring(string: str, substring: str, ignoreCase=True) -> int:
    if ignoreCase:
        string = string.lower()
        substring = substring.lower()
    return string.count(substring)

s = input("Enter a string: ")
sub = input("Enter a substring: ")
print(f"{sub} occured {countSubstring(s, sub)} times in {s}")