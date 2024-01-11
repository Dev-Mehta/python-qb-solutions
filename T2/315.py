"""
315 - Write a python program to reverse a string
"""

def reverse(string: str) -> str:
    # Method 1
    method_1 = string[::-1]
    # Method 2
    method_2 = ''
    for i in string:
        method_2 = i + method_2
    # Method 3
    method_3 = ""
    for i in range(len(string)-1, -1, -1):
        method_3 += string[i]
    # Method 4
    method_4 = "".join(reversed(string))
    # Method 5
    method_5 = list(string)
    method_5.reverse() # List function
    method_5 = "".join(method_5)
    assert method_1 == method_2 == method_3 == method_4 == method_5
    # The above statement is used to test if all values are same. 
    # ie. the answer is correct using all methods
    # If the condition is false, it will give assertionerror
    return method_1

print(reverse(input("Enter a string: ")))
