# Write python program to count the number of lines in a file
x = input("Enter file name: ")
with open(x) as f:
    print(len(f.readlines()))