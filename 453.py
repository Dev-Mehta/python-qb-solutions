# Taking input
l = input("Enter string of ints seperated by comma(,): ").split(",")
l = [int(x) for x in l]

o = list(filter(lambda x: x%13==0 or x%19==0, l))
print(o)
