"""
Write a python program to create a directory and 
subdirectory. It should print the current working directory path 
and list of names of files present in the given directory.
"""
from pathlib import Path
import os
cwd = Path(__file__).resolve().parent
dirr = input("Enter name of directory: ")
subdirectory = input("Enter name of subdirectory: ")
os.mkdir(cwd / dirr)
os.mkdir(cwd / dirr /subdirectory)
print(os.getcwd())
print(os.listdir())