"""
462: 
Create a python program which takes password as input and a function which checks whether the given password is valid or 
not under following conditions without using the RegEx module in Python language. 
Conditions required for a valid password:
1.	Password strength should be at least 8 characters long
2.	Password should contain at least one uppercase and one lowercase character.
3.	Password must have at least one number.

"""
def isValid(string: str) -> bool:
    explanation = ""
    minchars = len(string) >= 8
    uppercase = any(x.isupper() for x in string)
    digit = any(x.isdigit() for x in string) 
    lowercase = any(x.islower() for x in string)
    if not minchars:
        explanation += "\nPassword should have minimum 8 characters."
    if not uppercase:
        explanation += "\nPassword should have atleast one uppercase character"
    if not digit:
        explanation += "\nPassword should have atleast one digit in it."
    if not lowercase:
        explanation += "\nPassword should have atleast one lowercase character"
    if len(explanation) > 0:
        print(explanation)
    return len(explanation) == 0

s = "It is valid password" if isValid(input("Enter a password: ")) else "It is invalid password" 
print(s)