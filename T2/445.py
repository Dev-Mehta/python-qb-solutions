# Taking input
l = input("Enter string of ints seperated by comma(,): ").split(",")
l = [int(x) for x in l]
# Filter
odd = list(filter(lambda x: x%2!=0, l))
largest = max(odd)
print(largest)

# No functions allowed.
largest = odd[0]
for i in range(1,len(odd)):
    if odd[i] > largest:
        largest = odd[i]
print(largest)