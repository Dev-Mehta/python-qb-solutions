def sum(l: list) -> int:
    _sum = 0
    for i in l:
        _sum += i
    return _sum
# Taking input
l = input("Enter string of ints seperated by comma(,): ").split(",")
l = [int(x) for x in l]
print(sum(l))
