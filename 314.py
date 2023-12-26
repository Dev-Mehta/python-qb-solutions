"""
314 - Write a python program to calculate sum and average of digits present in a string
"""

def calculate(string: str) -> (int, int):
    def average(l: list):
        return sum(l) / len(l)
    l = []
    for i in string:
        if i.isdigit():
            l.append(int(i))
    return sum(l), average(l)

string = input("Enter a string: ")
s, a = calculate(string)
print(f"Sum: {s}, Average: {a}")