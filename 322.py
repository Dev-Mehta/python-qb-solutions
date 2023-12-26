"""
322 - Write a program to find maximum and minimum elements in tuple
"""
from ast import literal_eval

# I have used literal_eval insteaf eval because literal_eval is safer
# users can enter any obnoxious python code which will be evaluated by eval
# but literal_eval will only accept literals - i.e - tuples, lists, strings, integers, etc.
# eval(print("Hi")) # will print hi on screen, whereas
# literal_eval(print("hi")) # will give ValueError: malformed node or string
t = literal_eval(input("Enter a tuple seperated by ,\nFor eg. 1,2,3: "))
print(f"Max: {max(t)}, Min: {min(t)}")