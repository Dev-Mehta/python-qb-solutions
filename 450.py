from ast import literal_eval
d = literal_eval(input("Enter a dictionary: "))
e = literal_eval(input("Enter another one: "))
d.update(e)
print(d)