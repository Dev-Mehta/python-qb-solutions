# Taking input
l = input("Enter string of ints seperated by comma(,): ").split(",")
l = [int(x) for x in l]
# Filter
even = list(filter(lambda x: x%2==0, l))
odd = list(filter(lambda x: x%2!=0, l))
print(even)
print(odd)