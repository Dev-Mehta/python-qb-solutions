"""
Write a Python program to count the frequency of words in a file
Example:
File 1: python1.txt
Friends are crazy, Friends are naughty !
Friends are honest, Friends are best !
Friends are like keygen, friends are like license key !
new We are nothing without friends, Life is not possible without friends !
"""

with open("522_ip.txt", "w") as f:
    f.write("""Friends are crazy, Friends are naughty !
Friends are honest, Friends are best !
Friends are like keygen, friends are like license key !
new We are nothing without friends, Life is not possible without friends !""")
    
with open("522_ip.txt") as f:
    words = " ".join(f.read().split()).split(" ")
    freq = {}
    for i in words:
        freq.update({i: freq.get(i,0)+1})
    # Just formatted dictionary according to output format in question
    output = str(freq).lstrip("{").rstrip("}").replace("'", "").replace(": ", "-")
    print(output)