from functools import reduce
perms = []
def permute(arr: list, perm: list):
    if len(arr) == 0:
        perms.append(perm)
    for i in range(len(arr)):
        nlist = arr.copy()
        nlist.pop(i)
        p = perm.copy()
        p.append(arr[i])
        permute(nlist, p)
def printPerms():
    for i in perms:
        for j in i:
            print(j, end=" ")
        print("")
l = input("Enter values seperated by comma(,): ").split(",")
l = [int(x) for x in l]
permute(l,[])
printPerms()
print("The following answeres are after excluding duplicates")
print("Unique values inside list: ", len(set(l)))
print("Product of values inside list: ", reduce(lambda x,y: x*y, set(l)))