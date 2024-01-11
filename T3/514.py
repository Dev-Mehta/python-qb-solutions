"""
Using a file which consists of multiple statements, find all the words from the file that can be made from all the characters 
of given user’s string.
Note: If user enters same characters multiple times in a string, then word from file will only be eligible for output if it 
contains that character for same or more number of times in it. (if file have apple, greenapple and user’s string is ‘aepe’ 
then output will only be greenapple. apple is not eligible as it contains e for 1 time only.
For example:
If a given file is:
    apple is fruit which is healthy
    greenapple is tasty and sweet
    oranges and bananas are good for health
    fruits are good source of vitamins
    
String entered by user: nas
Output words will be: oranges, bananas, vitamins
String entered by user: isi
Output words will be: vitamins
String entered by user: eee
Output words will be: greenapple
"""

with open("514_ip.txt") as f:
    content = f.readlines()
    words = set()
    for i in content:
        words.update(i.split("\n")[0].split(" "))
    search_str = input("Enter string to search for: ")
    output = []
    for word in words:
        _word = word[::]
        for i in search_str:
            _word = _word.replace(i, "", 1)
        afterRemoval = len(_word)
        if len(word) - afterRemoval == len(search_str):
            output.append(word)
    print(output)