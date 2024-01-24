"""
Write a python program to read a text file “Story.txt” and print only word starting with ‘I’ in reverse order.
Example: If value in text file is : ‘INDIA IS MY COUNTRY’
Output will be: ‘AIDNI SI MY COUNTRY’
"""

with open("517_ip.txt") as f:
    content = f.readlines()

for line in content:
    words = line.strip("\n").split(" ")
    words = [word[::-1] if word[0].lower() == 'i' else word for word in words]
    words = " ".join(words)
    print(words)