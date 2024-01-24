"""
Write a Python program to count words, characters and spaces from text file.
Input:
Python is a Easy Subject
OOPs is One of the most
interesting Topic
Output:
No of space: 10
No of word: 13
No of character: 64
"""

content = """Python is a Easy Subject
OOPs is One of the most
interesting Topic"""
x = open("518_input.txt", "w")
x.write(content)
x.close()

with open("518_input.txt") as f:
    content = f.read()
    x =" ".join(content.split("\n"))
    print(x)
    print("No of space:", content.count(" "))
    print("No of words:", len(x.split(" ")))
    print("No of characters:", len(content) - content.count("\n"))