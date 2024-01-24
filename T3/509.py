# 509 Write a Python program to copy the contents 
# of a file to another file.
# 7 marks no che aa :)
a = input("Enter name of file 1: ")
b = input("Enter name of file 2: ")

open(b, "w").write(open(a, "r").read())
