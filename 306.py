"""
306 - Write a python program to check if a string is palindrome or not
"""

def isPalindrome(string: str) -> bool:
    """
    Returns whether the given string is palindrome or not
    Parameters:
        string (str): The string to check whether it is palindrome
    Returns:
        bool: True if string is palindrome else False
    """
    return string == string[::-1]

s = input("Enter a string: ")
output = "Given string is palindrome" if isPalindrome(s) else "Given string is not palindrome"
print(output)