# Taking input
l = input("Enter string of ints seperated by comma(,): ").split(",")
l = [int(x) for x in l]
# Filter
even = list(filter(lambda x: x%2==0, l))
# List comprehension
evens = [x for x in l if x % 2 == 0]
print(even)
print(evens)