# File Name learn_tuple.py
# Demo for basic Python tuple functionality
# link : https://www.tutorialspoint.com/python3/python_tuples.htm
#!usr/bin/python3

from utility import *
printDes("Tuple", "Tuple is combination of data like list but immutable. Here is some operations on tuple")
tuple1 = (1, "X", ["L", "B"])
tuple2 = (0,1,7,9,21,32)

# Accessing Tuple
printDes("Accessing tuple")
print("1. single access: ", tuple1, "[2] : ", tuple1[2])
print("2. sequence access: ", tuple2,"[2:4] : ", tuple2[2:4])

# Built-in Methods
printDes("Userful Methods")
# ==
tuple3 = (0,1,7,9,21,32)
print("1. comare(", tuple2,",",tuple3," = ", tuple2 == tuple3)
# tuple: Convert list into tuple
list1 = ["Hum", "Tum", "aur", "woh"]
tuple4 = tuple(list1)
print("2. converting list: ", list1, " to tuple: ", tuple4)

# max, min len: Same as list
printDes("END")
