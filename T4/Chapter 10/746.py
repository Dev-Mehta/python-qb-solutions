import matplotlib.pyplot as plt

plt.subplot(3,2,1)
plt.plot([5,10,25,60,80],[10,17,25,40,30], 'g:D')
plt.xlabel('x')
plt.ylabel('y')
plt.title('plot-1')

plt.subplot(3,2,2)
men = (22,30,35,35,26)
women = (25,32,30,35,29)
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
bar_positions_men = range(len(groups))
bar_positions_women = [pos + 0.35 for pos in bar_positions_men]
plt.bar(bar_positions_men, men, color='green', width=0.35,label='Men')
plt.bar(bar_positions_women, women, color='red', width=0.35,label='Women')
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Bar Plot of Scores by Group and Gender')

plt.subplot(3,2,3)
plt.pie([25,50,30,20,35], labels=['Maruti Suzuki', 'Hyundai', 'Kia', 'Toyota', 'Honda'], autopct='%1.2f%%')

math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]

plt.subplot(3,2,4)
plt.scatter(range(1, 11), math_marks, color='yellow', marker='o',label='Mathematics')
plt.scatter(range(1, 11), science_marks, color='blue', marker='*', label='Science')
# Subplot 5
plt.subplot(3, 2, 5)
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C', 'C++']
popularity_languages = [20, 100, 25, 30, 45, 50]
plt.barh(languages, popularity_languages, color=['orange', 'green', 'blue','red', 'purple', 'pink'])
plt.xlabel('Popularity')
plt.ylabel('Prog Lang')
plt.title('Popularity of Programming Languages')
# Subplot 6
plt.subplot(3, 2, 6)
data_histogram = [10, 20, 20, 30, 30, 30, 40, 40, 40, 40, 50, 50, 50, 60, 60,70]
plt.hist(data_histogram, color='red', bins=10, edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram Chart')
plt.tight_layout(w_pad=20.0)
plt.show()