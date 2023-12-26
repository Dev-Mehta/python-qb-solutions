"""
318 - Write a python program to capitalize first and last character
of each word from a given string
"""

def createStr(string: str) -> str:
    words = string.split()
    for i in range(len(words)):
        word = words[i]
        word = word.replace(word[0], word[0].upper())
        word = word.replace(word[-1], word[-1].upper())
        words[i] = word
    return " ".join(words)

print(createStr(input("Enter a string: ")))