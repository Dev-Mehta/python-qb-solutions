import os

os.mkdir("mystringmodule")
os.chdir("mystringmodule")

with open("mystring.py", "w") as f:
    code = """def count(s: str, sub: str, start=None,end=None) -> int:
    return s.count(sub,start,end)

def find(s: str, sub: str, start=None, end=None) -> int:
    return s.find(sub,start,end)"""
    f.write(code)

with open("540_answer.py", "w") as f:
    code = """
import mystring as m
s = input("Enter a string: ") # for eg Hello Hi Hey
sub = input("Enter a substring: ") # He
print(m.count(s,sub)) # 2
print(m.find(s,sub)) # 0"""
    f.write(code)
    
