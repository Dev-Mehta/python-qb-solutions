"""
Write a function count_lines() to count and display the total number of lines from the file. Consider the following lines for 
the file – friends.txt.
Friends are crazy, Friends are naughty !
Friends are honest, Friends are best !
Friends are like keygen, friends are like license key !
We are nothing without friends, Life is not possible without friends !
"""
from helper import *

content = """Friends are crazy, Friends are naughty !
Friends are honest, Friends are best !
Friends are like keygen, friends are like license key !
We are nothing without friends, Life is not possible without friends !"""

f = File("tmp.txt", "w+", content=content)
f.save_as("505_friends.txt")
f.delete()

with open("505_friends.txt") as f:
    print("Number of lines:", len(f.readlines()))
    