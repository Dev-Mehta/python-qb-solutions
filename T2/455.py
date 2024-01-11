"""
Given a list of elements, write a python program to perform grouping of similar elements, as different key-value list in 
dictionary. Print the dictionary sorted in descending order of frequency of the elements.
Note: To perform the sorting, use the sorted function by converting the dictionary into a list of tuples. After sorting, convert 
the list of tuples back into a dictionary and print it.
Input : test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8] 
Output : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]} 
Explanation : Similar items grouped together on occurrences. 
Input : test_list = [7, 7, 7, 7] 
Output : {7 : [7, 7, 7, 7]} 
Explanation : Similar items grouped together on occurrences.
"""

l = input("Enter string of ints seperated by comma(,): ").split(",")
l = [int(x) for x in l]
d = {}
for i in l:
    x = d.get(i, [])
    x.append(i)
    d.setdefault(i, x)
print(d)