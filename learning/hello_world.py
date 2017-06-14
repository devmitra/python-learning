# File Name hello_world.py
# Demo for basic Python functionality
#!usr/bin/python3
import sys

# If-else
print("Hello World - Python - Pushan Mitra")
if True:
   print ("Answer")
   print ("True")

else:
   print ("Answer")
   print ("False")

# Generator
def fibonacci(n): #generator function
   a, b, counter = 0, 1, 0
   while True:
      if (counter > n):
         return
      yield a
      a, b = b, a + b
      counter += 1
f = fibonacci(5) #f is iterator object

#Usage of Generator
while True:
   try:
       print (next(f), end=" ")
   except StopIteration:
       print ("\n")
       break

# Generator : Generator of first N integers
def firstN (n):
    num = 0;
    while num < n:
        yield num
        num += 1

fnew = firstN(8)
print("First N \n")
# for in loop using generator
for n in fnew:
    print(n, end = " ")


# Type Checking
str1 = "This is a string"
print("\nType of str1 is str? ", type(str1) is str)
print("\n Type of str1:", type(str1))
print("\n str1 is instance of:", isinstance(str1, str))
#print("\n str1 is instance of:", isinstance(str1, (str, unicode)))


input("\n\nPress the enter key to exit.")
