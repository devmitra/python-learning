# File Name learn_string.py
# Demo for basic Python string functionality
#!usr/bin/python3
import sys

# Print str struct
print(" str \n")
print(str)
print("\n end:str \n")

# Simple String object

str1 = "Hello world"
str2 = 'This is string too'

# Access unit single char : Operator [idx]
c = str1[0]
print("\n First char of str1 = ", c)
print("\n Type of c =", type(c))

# Get SubString till index  : Operator: [:index]
sub6 = str1[:6]
print("\n SubString till index:6, sub6 = ", sub6)

# Get SubString from index  : Operator: [index:]
subStr = str1[2:]
print("\n SubString from index:2, subStr = ", subStr)

# Sequence : Operator: [start:end]
sq = str2[1:7] # Sequence of 1 to 7
print("\n sq = ", sq)

# Updating a string and storing
str3 = str1[:6] + "laba"
print("\n Update str1 = str1[:6] + 'laba' = str3 = ", str3)

# Repeat
str3 = "Laba "
strRepeat = str3 * 3
print("\n Repeat of 'Laba' = ", strRepeat)

# Membership
strMem = "X is here"
print("\n Membership of 'X': ", 'X' in strMem)
print("\n Not Membership of 'Y': ", 'Y' in strMem)

# Formatting
print("\n String Formatting")
formatStr = "[1]:This is %s, my age is %d" % ('Pushan', 32)
print("\n", formatStr)
floatVar = 11 / 3
print("\n Float Format : %0.7f" % floatVar)
print("\n Float Format : {0:.3f}".format(floatVar))

# Triple Quote : Multiline string
triple = """ I am having good time with my family.Life is good if are in right place with right people.
            \n Long ago I realize that."""
print(triple)

# Userful methods
# link : https://www.tutorialspoint.com/python3/python_strings.htm
