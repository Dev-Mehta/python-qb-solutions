def sum(*args):
    s = 0
    for i in args:
        s += i
    return s 

def sub(*args):
    s = args[0]
    args = args[1:]
    for i in args: 
        s -= i 
    return s

def mul(a, b):
    return a * b

def div(a, b):
    return a / b