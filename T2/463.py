hashmap = {}
s = input("Enter a string: ")
s = s.split(" ")
for key in s:
    value = hashmap.get(key.lower(), 0) + 1
    hashmap.update({key.lower():value})
print(hashmap)