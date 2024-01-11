"""
310 - Write a python program to demonstrate negative index in tuple
"""

def demonstrate(t: tuple) -> None:
    if len(t) == 0:
        print("You entered empty tumple")
        return
    print("Accessing based on negative index")
    for i in range(-len(t), 0):
        print(f"Index: {i}, Value: {t[i]}")
t = (1,5,4,3,8,6,8)
demonstrate(t)