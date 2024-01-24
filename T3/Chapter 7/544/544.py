"""
Write a python program to copy content of File1
into File2 in which all lines of a file1 or remaining 
portion of line except those that have hash sign (#) 
(means comments).
"""

from filemodule import copyfile

f1 = open("file1.txt", "w")
f1.write("""# Hello LJ
Wish you happy Republic #Day
Happy 74th Republic Day
What a #Parade at Kartavya Path
Very Happy after watching that parade""")
f1.close()
copyfile("file1.txt", "file2.txt")