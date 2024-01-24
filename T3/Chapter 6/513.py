"""
Write a “pager” program. 
Your solution should prompt for a filename, 
and display the text file 25 lines at a time, pausing 
each time to ask the user to enter the word “continue”,
in order to show the next 25 lines or enter 
the word “stop” to close the file.
"""

n = 25
with open("513_input.txt") as f:
    for index, line in enumerate(f,1):
        print(f"{index}:{line}", end="")
        if index % n == 0:
            q = input("Enter stop to stop, continue to continue: ")
            while q.lower() not in ["continue", "stop"]:
                print("Please enter a valid input")
                q = input("Enter stop to stop, continue to continue: ")
            if q.lower() == "stop":
                break