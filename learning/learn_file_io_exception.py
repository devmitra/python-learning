# File Name learn_file_io_exception.py
# Demo for basic file operation in python3 and also explan exception handling
# link : https://www.tutorialspoint.com/python3/python_files_io.htm
#!usr/bin/python3

# System module
import os

# Local modules
from utility import *

printDes("Python File operations")

# Open a file
# Mode:
#   r   : Read, file pointer at beginning
#   r+  : Read/write,  file pointer at beginning
#   rb  : Read binary, file pointer at beginning
#   rb+ : Read/write binary mode, file pointer at beginning
#   w   : write, file pointer at beginning
#   w+  : Write/Read,file pointer at beginning. Overwrites the existing file if the file exists.
#           If the file does not exist, creates a new file for reading and writing.
#   wb  : same as w with binary Mode
#   wb+ : same w+ with binary mode.

# Create File
filepath = "./tmp/labaText.tmp.txt"
fo = open(filepath, "w")
fo.write("Hello world from Laba");
fo.close()

# Read File
fr = open(filepath, "r")
strr = fr.read(100) # read whole file strr = fr.read()
print("The value of file @ ", filepath, " => ", strr)

# Rename file
os.rename("./tmp/labaText.tmp.txt", "./tmp/gasText.tmp.txt")

# Remove File
os.remove("./tmp/gasText.tmp.txt")

# Create dir: Also example of exception handling
try:
    os.mkdir("./tmp/laba")
except IOError as excp:
    print("Exception: ", excp)
try:
    os.mkdir("./tmp/gas")
except IOError as excp:
    print("Exception: ", excp)

# Remove dir
os.rmdir("./tmp/gas")

# Get current working dir
wd = os.getcwd()
print("Current working dir => ", wd)

printEnd()
