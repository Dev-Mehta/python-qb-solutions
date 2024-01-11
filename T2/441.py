# Taking input
l = input("Enter string of ints seperated by comma(,): ").split(",")
l = [int(x) for x in l]
# Map
doubled = list(map(lambda x: x*2, l))
print(doubled)