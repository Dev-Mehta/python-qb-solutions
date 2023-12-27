from functools import reduce
# Taking input
l = input("Enter string of ints seperated by comma(,): ").split(",")
l = [int(x) for x in l]

pos_sum = reduce(lambda x, y: x+y, list(filter(lambda x: x > 0, l)))
neg_sum = reduce(lambda x, y: x+y, list(filter(lambda x: x < 0, l)))
print(pos_sum)
print(neg_sum)