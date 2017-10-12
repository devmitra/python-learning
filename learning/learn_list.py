# File Name learn_list.py
# Demo for basic Python list functionality
# link : https://www.tutorialspoint.com/python3/python_lists.htm
#!usr/bin/python3

# Utility
# Print Section Header and description with Format
def printDes(sectionHeader, description = ""):
    print("\n---- %s ----" % sectionHeader)
    if description:
        print(" %s" % description)
        print("----------------------------------------------------------------")

    print("\n")
    return
def strList(list, sep = " "):
    #return "".join('{}'.format(k) for k in list).join(sep)
    res = "[ "
    for k in list:
        res = res + "".join('{}'.format(k)) + sep
    return res + "]"
##############################################################
printDes("Tutorial of Python List operations", """The whole file contains small exaples of python list operations""")

# Creating Few List
listNum = [0,1,2,3,4,5,6,7,8,9]
listAlpha = ["a","b","c","d","e"]
listOfList = [listNum, listAlpha]
listOfFriends = ["Laba", "Pungi", "Lej", "Dim", "Doggy", "Lele"]
listRandom = [1, "x", "GOL", 6]

# Str List
printDes("Testing strList: Convert List to string")
print(strList(listOfFriends))

# Getting value from List
printDes("Accessing List")
print("case1: Get single item : lisntNum[3] = ", listNum[3])
print("case2: Get sub sequence: listNum[1:5] = ", listNum[1:5])
# Update
printDes("Update list item")
print("case1: upldate: before update: listRandom: %s" % strList(listRandom))
listRandom[2] = "y"
print("case1: after update: listRandom: %s" % strList(listRandom))
# Delete
printDes("Delete item from List")
print("case1: delete: before delete: listRandom: %s" % strList(listRandom))
del listRandom[2]
print("case1: delete: after delete: listRandom: %s" % strList(listRandom))
# String operations
printDes("Some string operations", "Some basic sring ops")
printDes("Length")
print("Length of the %s is " % strList(listOfFriends), len(listOfFriends))
printDes("Membership")
print("Item %s is available in %s :" % ("Laba", strList(listOfFriends)), "Laba" in listOfFriends)
print("Item %s is available in %s :" % ("Mano", strList(listOfFriends)), "Mano" in listOfFriends)
printDes("Repetition")
smallList = [2,7]
print("%s * 3 = " % (smallList), smallList * 3)
# Indexing, Slicing
printDes("Indexing, Slicing", "Sama as string")
printDes("Indexing")
print("case1: Indexing: Positive value indexing: index 2 of %s is ", strList(listOfFriends), listOfFriends[2])
print("case2: Indexing: Negative value indexing: index -2 of %s is ", strList(listOfFriends), listOfFriends[-2])
printDes("Slicing")
print("Slice of %s : [:2] is %s" % (strList(listOfFriends), strList(listOfFriends[:2])))
print("Slice of %s : [3:] is %s" % (strList(listOfFriends), strList(listOfFriends[3:])))
# Built-in Methods
printDes("Some important built-in function for List")
print("Max: max of %s" % strList(listNum), max(listNum))
print("Min: min of %s" % strList(listNum), min(listNum))
print("List From Sequence")
tup = (2,"GG", "PAN", 7, 9)
print("case1: From Tuple: ",tup, " => ", list(tup))
str1 = "Ye bik gayi hai gormint"
print("case2: From string:", str1, " => ", list(str1))

# List - Methods
printDes("Some Userful List methods")
print("\n\n---- END:LIST ----\n\n")
