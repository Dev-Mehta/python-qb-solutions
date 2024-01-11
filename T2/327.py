"""
327: Write a program to check validity of password
Conditions: 
Minlength: 8, Min 1 Uppercase, Min 1 Digit, Min 1 Special Char of ($, @, _)
"""
def isValid(string: str) -> bool:
    explanation = ""
    minchars = False
    allowed_char = ['$', '@', '_']
    uppercase = any(x.isupper() for x in string)
    digit = any(x.isdigit() for x in string) 
    spec_char = any((x in allowed_char) for x in string if not (x.isdigit() or x.isalpha()))
    if len(string) >= 8:
        minchars = True
    if not minchars:
        explanation += "\nPassword should have minimum 8 characters."
    if not uppercase:
        explanation += "\nPassword should have atleast one uppercase character"
    if not digit:
        explanation += "\nPassword should have atleast one digit in it."
    if not spec_char:
        explanation += f"\nPassword should have atleast one of these special characters\n{allowed_char}"
    if len(explanation) > 0:
        print(explanation)
    return len(explanation) == 0

s = "It is valid password" if isValid(input("Enter a password: ")) else "It is invalid password" 
print(s)