"""
Given a list L of size N, You need to count the number of special elements in the given list. An element is special if 
removal of that element makes the list balanced.
The list will be balanced if sum of even index elements is equal to the sum of odd index elements.
Example Input
Input 1:
A = [2,1,6,4]
Input 2:
A=[5,5,2,5,8]
Example Output
Output 1:
1
Output 2:
2
Explanation 1 :
After deleting 1 from list : [2,6,4]
(2+4) = (6)
"""

def checkBalance(l: list, n: int) -> int:
    count = 0
    for i in range(n):
        t = l.copy()
        t.pop(i)
        sum_even, sum_odd = sum([t[x] for x in range(n-1) if x%2==0]), sum([t[x] for x in range(n-1) if x%2!=0])
        if sum_even == sum_odd:
            count += 1
    return count
from ast import literal_eval
l = literal_eval(input("Enter a list seperated by commas: "))
print(checkBalance(l, len(l)))