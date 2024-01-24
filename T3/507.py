"""
Write a Python program to read a text file and do following: 1. Print no. of words 2. Print no. statements
"""
from helper import *
from string import punctuation

f = File("505_friends.txt")
content = f.read()
trans = str.maketrans('', '', punctuation)
content = content.translate(trans)
print("Words: ", len(content.split(" ")))
print("Lines: ",len(content.split("\n")))