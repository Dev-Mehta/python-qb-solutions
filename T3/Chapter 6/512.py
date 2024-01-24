# Write a python program to search for a string in text files. 
s = input("Enter a string to search for: ")
x = input("Enter file name: ")
with open(x) as f:
    content = f.read()
    if s in content:
        print("Found at", content.find(s))
    else:
        print("Could not find", s)