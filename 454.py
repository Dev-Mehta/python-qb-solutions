# Taking input
l = input("Enter string of ints seperated by comma(,): ").split(",")
l = [int(x) for x in l]
key = int(input("Enter the key: "))
for i in range(len(l)):
    if l[i] == key:
        print(f"{key} was found at index {i}.")
        break