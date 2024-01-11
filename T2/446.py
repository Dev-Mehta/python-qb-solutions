# Taking input
l = input("Enter string of ints seperated by comma(,): ").split(",")
l = [int(x) for x in l]
if len(l) < 2:
    print("Min. 2 elemenets required")
else:
    c = l[::-1]
    l[0] = c[0]
    l[-1] = c[-1]
    print(l)