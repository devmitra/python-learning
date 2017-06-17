# File Name learn_string.py
# Demo for basic Python string functionality
# link : https://www.tutorialspoint.com/python3/python_strings.htm
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
# length : length of the string
print("------- Testing : len() -------")
print("[%s] length: " % formatStr ,  len(formatStr))
# count : String Inclusion with count of sub string
bigStr = 'Here I am, this is me, no where else you can find me'
test1 = 'this is me'
test2 = 'laba'
test3 = 'me'
print("------- Testing : count() -------")
print("count  - test1 = " , bigStr.count(test1))
print("count  - test2 = " , bigStr.count(test2))
print("count  - [%s] = " % test3 , bigStr.count(test3))

# find : String Inclusion with first index of sub string
print("------- Testing : find() -------")
xString = "1x xx2 xy4 np7 np4"
print("find x : ", xString.find('x'))
print("find np", xString.find('np'))

# endswith : Sufix test
print("------- Testing : endswith() -------")
suffix = "find me"
print(" [%s] is Sufix of [%s]? " % (suffix, bigStr), bigStr.endswith(suffix))
# startswith : Prefix test
print("------- Testing : startswith() -------")
prefix = "Here I am"
print(" [%s] is Prefix of [%s]? " % (prefix, bigStr), bigStr.startswith(prefix))


# String Contain Testing
# Different strings
alphanum = "abc12x98"
alpha = "abcwer"
numHex = "%X" % 6785
num = "1298"
numfloat = "12.980"
# isalnum() : Alpha-numeric testing
print("------- Testing : isalnum() -------")
print("[%s] is alpha-num? " % alphanum, alphanum.isalnum())
# isalpha()
print("------- Testing : isalpha() -------")
print("[%s] is alpha? " % alphanum, alphanum.isalpha())
print("[%s] is alpha? " % alpha, alpha.isalpha())
# isdigit()
print("------- Testing : isdigit() -------")
print("[%s] is digit? " % numHex, numHex.isdigit())
print("[%s] is digit? " % num, num.isdigit())
print("[%s] is digit? " % numfloat, numfloat.isdigit())
# isnumeric
print("------- Testing : isnumeric() -------")
print("[%s] is numeric? " % numHex, numHex.isnumeric())

# Case functions : isupper() islower() upper() lower() swapcase()

# Replace
print("------- Testing : replace() -------")
print("[%s] replacing [%s] with LAO: %s" % (xString, 'np', xString.replace('np', 'LAO')))

# Striping : Removing whitespace : lstrip() rstrip() strip()
stripString = "   Laba asche tere    "
print("[%s] is stripped and result = [%s]" % (stripString,stripString.strip()) )

# Padding ljust() rjust()
print("------- Testing : ljust() -------")
str = "this is string example....wow!!!"
print (str.ljust(50, '*'))
