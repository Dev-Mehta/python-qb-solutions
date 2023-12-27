stack = []
import os
os.system("@echo off")
while True:
    os.system("cls")
    explanation = """
    1. Enter [1] for adding element in stack.
    2. Enter [2] for removing element in stack.
    3. Enter [3] for clearing stack.
    4. Enter [4] for printing stack.
    5. Enter [e] for exiting program
    """
    print(explanation)
    cmd = input("Enter a your option: ")
    match(cmd):
        case "e":
            break
        case "E":
            break
        case "1":
            e = int(input("Enter your element: "))
            stack.append(e)
            input()
        case "2":
            print(f"Popped {stack.pop()} from stack")
            input()
        case "3":
            stack.clear()
            print(stack)
            input()
        case "4":
            print(stack[::-1])
            input()
        case _:
            print("Invalid input")
            input()
os.system("@echo on")