from ast import literal_eval
from functools import reduce

# Part A
l = literal_eval(input("Enter a list. Eg: [1,2,3] : "))
t = tuple(map(lambda x: str(x), l))
print(type(t))
print(t)

# Part B
l = literal_eval(input("Enter a list. Eg: [1,2,3] : "))
l = list(map(lambda x: x*10, l))
print(l)

# Part C
l = literal_eval(input("Enter a list. Eg: [1,2,3] : "))
product = reduce(lambda x,y: x*y, l)
print(product)

# Part D
def countChar(s, c):
    count = 0
    for i in s:
        if i == c:
            count += 1
    return count
s = input("Enter a string: ")
c = input("Enter the char: ")
print(countChar(s,c))

# Part E
def findChar(s, c):
    for i in range(len(s)):
        if s[i] == c:
            return i
    return -1
s = input("Enter a string: ")
c = input("Enter the char: ")
print(findChar("Dev Mehta", "e"))

