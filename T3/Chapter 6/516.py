# Write a python program to extract a list of all four-letter words that start and 
# end with the same letter from a given text file

with open("516_input.txt", "w") as f:
    words = ['test', 'papa', 'area', 'height', 'Text', 'paap', 'himalay', 'ymca', 'pmyp']
    words = list(map(lambda x: x + "\n", words))
    f.writelines(words)

with open("516_input.txt") as f:
    words = f.read().split()
    words = [word for word in words if len(word) == 4 and (word[0] == word[-1])]
    for i in words:
        print(i)