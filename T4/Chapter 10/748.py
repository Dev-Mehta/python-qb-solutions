import numpy as np

scores = np.array([[31, 12, 19, 53],
 [67, 48, 95, 83],
 [59, 67, 13, 59],
 [62, 29, 99, 88],
 [87, 91, 69, 76]])
# 1
print("Maximum score in T_20-3:", np.max(scores[:, 2]))
# 2
print("Maximum score of Yuvraj: ", np.max(scores[2]))
# 3
sum = np.sum(scores, axis=1)
scores = np.column_stack((scores, sum))
print(scores)
# 4
print("""4. Sort the array (non-ascending order) on the total score of each
batsman column (one added in the above task.) and print the sorted array.
""")
print(scores[np.argsort(scores[:, -1])[::-1]])
# 5
print("""5.make a new array with the sum of all five-batsman runs of each match␣
and print a new array (use only the numpy module)""")
scores = scores[:, 0:4]
sum = np.sum(scores, axis=0)
print(np.row_stack((scores, sum)))
# 6
print("""6. make a new array which represents if the batsman’s score greater than
30 denote 1 else 0(use only the numpy module)""")
print(np.where(scores[:, :-1] > 30, 1 ,0))
# 7
print("""7.Create a Histogram of the SACHIN score in all matches,
showing the frequency count in a range of 0-20,20-40, and 40-60. (use the␣
Scores array for the SACHIN score)""")
import matplotlib.pyplot as plt
plt.hist(scores[0], bins=[0,20,40,60])
plt.show()