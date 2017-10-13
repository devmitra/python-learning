# File Name learn_dict.py
# Demo for basic Python Dict functionality
# link : https://www.tutorialspoint.com/python3/python_dictionary.htm
#!usr/bin/python3

from utility import *
printDes("Dictionary", """Dictionary is key value storage for python.
Each key must be unique, immutable like string, number, tuple.
Value can be any type object""")
# Dec
dict1 = {"key1": "Laba", "key2" : 5, (2,3) : [2,3]}

# Access and Update
printDes("Access, Update, Delete")
dict2 = dict(dict1)
# access
print("1. access:accessing data from dict: ", dict1,"[key2] : ", dict1["key2"])
#update
dict2["key2"] = "Newyork"
print("2. update:update data on dict: ", dict1, " updating dict1[\"key2\"] = \"Newyork\" => ", dict2)
#delete
dict3 = dict(dict1)
del dict3["key1"]
print("3. delete:remove key from dict: ", dict, " removing \"key1\" => ", dict3)

# Userful built-in function
printDes("Userful built-in function")
# str
print("str: Create printable version of dict: ", str(dict1))

printDes("END")
