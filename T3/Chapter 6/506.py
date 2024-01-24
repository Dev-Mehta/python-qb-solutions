# Write a function display_oddLines() to display odd number lines from the text file.
def display_oddLines(filename):
    with open(filename) as f:
        l = f.readlines()
        l = [l[i] for i in range(len(l)) if i % 2 == 0]
        for i in l:
            i = i.split("\n")[0]
            print(i)

display_oddLines("505_friends.txt")