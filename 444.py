# Taking input
l = input("Enter string of ints seperated by comma(,): ").split(",")
l = [int(x) for x in l]
# Filter
even = list(filter(lambda x: x%2==0, l))
largest = max(even)
print(largest)

# No functions allowed.
largest = even[0]
for i in range(1,len(even)):
    if even[i] > largest:
        largest = even[i]
print(largest)