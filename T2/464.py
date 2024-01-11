"""
464: 
Write a python Program to check entered password by user is correct or not. Entered password is correct if it has upper 
character, lower character , digits (but not more than 3 digits) ,special character and length is greater than or equal to eight 
and less than equal to fifteen. Get the digits from entered password and convert it in to number and then convert it in to 
English Word .
Example:
case 1
pw= R@m@3fa1tu9e$
Valid Password
num= 319
three hundred and nineteen
case 2
pw= S@m@6a1tue$
Valid Password
num= 61
sixty-one
case 3
pw= S@m@6a26u8$
Invalid Password

"""
def numtowords(string: str):
    d = d = {11:"Eleven", 12:"Twelve", 13: "Thirteen", 
                14: "Fourteen", 15:"Fifteen", 16:"Sixteen",
                   17:"Seventeen",18:"Eighteen", 19:"Nineteen", 
                   1: "One", 2:"Two", 3:"Three", 4:"Four",
              5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 
              9:"Nine", 0: "Zero", 10: "Ten",20: "Twenty", 30: "Thirty", 40: "Forty", 50:"Fifty",
                 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
    if len(string) == 1:
        return d[int(string)]
    if len(string) == 2:
        try:
            return d[int(string)]
        except KeyError:
            n = int(string)
            return d[n-n%10] + "-" + d[n%10]
    if len(string) == 3:
        n = int(string[1:])
        try:
            return d[int(string[0])] + " Hundred And " + d[n]
        except KeyError:
            return d[int(string[0])] + " Hundred And " + d[n-n%10] + "-" + d[n%10]
def isValid(string: str) -> (bool, str) :
    minchars = len(string) in range(8,16)
    uppercase = any(x.isupper() for x in string)
    digits = [x for x in string if x.isdigit()]
    digit = len(digits) in range(1,4) 
    lowercase = any(x.islower() for x in string)

    return minchars and uppercase and digit and lowercase, numtowords("".join(digits))
valid, num = isValid(input("Enter a password: "))
s = "It is valid password" if valid else "It is invalid password" 
print(s)
print(num)