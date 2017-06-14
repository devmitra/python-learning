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

while True:
   try:
       print (next(f), end=" ")
   except StopIteration:
       print ("\n")
       break

def firstN (n):
    num = 0;
    while num < n:
        yield num
        num += 1

fnew = firstN(8)
print("First N \n")
while n in fnew
    print(n, end = " ")

input("\n\nPress the enter key to exit.")
