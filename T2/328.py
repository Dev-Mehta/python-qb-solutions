"""
328: Change case of characters
"""
def changeCase(string: str) -> str:
    string = list(string)
    for i in range(len(string)):
        string[i] = string[i].upper() if string[i].islower() else string[i].lower()
    return "".join(string)
print(changeCase(input("Enter a string: ")))