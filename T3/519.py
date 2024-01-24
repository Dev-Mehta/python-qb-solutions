"""
File Filtering. write all lines of a file1, except those that start with a pound sign ( # ), the comment character for Python to 
file2. And display data of file2.
Text file1 content:
Friends are crazy, Friends are naughty ! 
#Friends are honest, Friends are best ! 
Friends are like keygen, #friends are like license key ! 
We are nothing without friends, Life is not possible without friends !
Text file2 shoud be:
Friends are crazy, Friends are naughty ! 
Friends are like keygen, 
We are nothing without friends, Life is not possible without friends !
"""
ip = """Friends are crazy, Friends are naughty ! 
#Friends are honest, Friends are best ! 
Friends are like keygen, #friends are like license key ! 
We are nothing without friends, Life is not possible without friends !"""
with open("519_input.txt", "w") as f:
    f.write(ip)

with open("519_input.txt") as f:
    lines = f.readlines()
    lines = [line.split('#')[0].strip() for line in lines]
    lines = [line for line in lines if line != '']
    lines = [line.split("\n")[0] + "\n" for line in lines]
    with open("519_output.txt", "w") as fo:
        fo.writelines(lines)