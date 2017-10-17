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
printDes("Useful built-in function")
# str
print("str: Create printable version of dict: ", str(dict1))

# Dictionary methods
printDes("Useful built-in method of dict struct.")
# clear
temp = dict(dict1)
temp.clear()
print("1. clear: Clearing all elemnets of dict:",dict1,"after clear: ",temp)
# copy
temp = dict1.copy()
print("2. copy: copying of dict1 =", dict1, " =>  temp = ", temp)
temp["lao"] = "Laba"
print("2. copy: Now updating temp = ", temp, ", dict1 = ", dict1)
# fromkeys
testDict = {"x1" : 1, "x2" : 2, "x3" : 3}
seq = {"x1", "x2"}
result = testDict.fromkeys(seq)
result1 = testDict.fromkeys(seq, 99)
print("3. fromkeys: Getting new dict with formkeys: testDict =", testDict," seq =", seq, " result=", result)
print("3. fromkeys: Getting new dict with formkeys with replacing with default new number:  testDict =", testDict," seq =", seq, " result=", result1)
# get
val = testDict.get("x2")
print("4. get: Get value:", testDict ,".get(\"x2\") = ", val)
val = testDict.get("x4", "Laba")
print("4. get: Get value and default value if value not exists: val = ",testDict,".get(\"x3\", \"Laba\") = ", val)
# items
print("5. items: Tuple of key value pair:", testDict, ".items() = ", testDict.items())
# keys and values : Creating list from dict_kyes and dic_values
keys = list(testDict.keys())
values = list(testDict.values())
print("6. kyes: all keys dict: ",testDict,".kyes() = ", keys)
print("7. values: all values of dict: ", testDict,".values() = ", values)
# update : updating one dict with values of other dict
oneDict = {"a" : "Laba", "b" : "Lao"}
temp = dict(testDict)
temp.update(oneDict)
print("8. update: ", testDict, ".update(", oneDict,") => ", temp)
# setdefault: get + set default value if value not exist
temp = dict(testDict)
temp.setdefault("x4", 4)
print("9. setdefault: ", testDict,".setdefault(\"x4\",4) = ",temp)
printDes("END")
