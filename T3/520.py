"""
Write a python program to accept
string/sentence from user till the user
enters “END”. Each string/sentence entered by 
user should be a newline in file. Save all the 
lines in file and display only those lines which begin
with capital letter.
"""

with open("520.txt", "w") as f:
    while True:
        line = input("Enter your line. Enter END to exit: ")
        if line == "END":
            f.close()
            break
        f.write(line + "\n")

with open("520.txt") as f:
    lines = f.read().split("\n")
    lines.pop()
    lines = [line for line in lines if line[0].isupper()]
    for line in lines:
        print(line)