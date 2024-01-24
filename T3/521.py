"""
Write a program to compare two text files. If they are different, give the line and column numbers in the files where the 
first difference occurs.
Example:
File 1: python1.txt
Friends are crazy, Friends are naughty !
Friends are honest, Friends are best !
Friends are like keygen, friends are like license key !
new We are nothing without friends, Life is not possible without friends !
File 2: python2.txt 
Friends are crazy, Friends are naughty !
Friends 6re honest, Friends are best !
Friends are like keygen, friends are like license key !
new We are nothing without friends, Life is not possible without friends ! 
Output:
line number 2 colNo. 9
"""

f1 = open("521_file1.txt", "w")
f2 = open("521_file2.txt", "w")
f1.write("""Friends are crazy, Friends are naughty !
Friends are honest, Friends are best !
Friends are like keygen, friends are like license key !
new We are nothing without friends, Life is not possible without friends !""")
f2.write("""Friends are crazy, Friends are naughty !
Friends 6re honest, Friexds are best !
Friends are like keygen, friends are like license key !
new We are nothing withodt friends, Life is not possible without friends !""")
f1.close()
f2.close()

f1 = open("521_file1.txt")
f2 = open("521_file2.txt")

f1_content = f1.readlines()
f2_content = f2.readlines()
f1.close()
f2.close()

try:
    for i in range(min(len(f1_content), len(f2_content))):
        line1 = f1_content[i]
        line2 = f2_content[i]
        for j in range(min(len(line1), len(line2))):
            if line1[j] != line2[j]:
                print(f"Line: {i+1}, Position: {j+1}, [{line1[j]}], [{line2[j]}]")
                # Remove below line to get all different positions output
                raise ValueError
        j += 1
        while j < len(line1):
            print(f"Line: {i+1}, Position: {j+1}")
            j += 1
        while j < len(line2):
            print(f"Line: {i+1}, Position: {j+1}")
            j += 1
    i += 1
    while i < len(f1_content):
        print(f"Line: {i+1}")
        i += 1
    while i < len(f2_content):
        print(f"Line: {i+1}")
        i += 1
except ValueError:
    pass