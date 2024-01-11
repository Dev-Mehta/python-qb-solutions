s = input("Enter a string: ")
shift = int(input("Enter shift: "))
result = ""
for i in range(len(s)):
    c = s[i]
    if c.isupper():
        result += chr((ord(c) + shift-65) % 26 + 65)
    elif c.islower():
        result += chr((ord(c) + shift-97) % 26 + 97)
    elif c.isdigit():
        result += chr((ord(c) + shift-48) % 10 + 48)
    else:
        result += c
print(result)