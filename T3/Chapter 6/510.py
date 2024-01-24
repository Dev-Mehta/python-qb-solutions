# Write a python program to read line by line 
# from a given files file1 & file2 and write into file3

"""
Write a python program to read line by line from a given file, file1 and file2 and write into file3
"""
f1 = open("file1.txt")
f2 = open("file2.txt")

f1_lines = f1.readlines()
f2_lines = f2.readlines()

f1.close()
f2.close()

f3 = open("file3.txt", "w")
for i in range(min(len(f1_lines), len(f2_lines))):
    f3.write(f1_lines[i])
    f3.write(f2_lines[i])
i += 1
if i < len(f1_lines):
    f3.writelines(f1_lines[i:])
else:
    f3.writelines(f2_lines[i:])
f3.close()