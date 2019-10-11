# File Name learn_list.py
# Demo for basic Python list functionality
# link : https://www.tutorialspoint.com/python3/python_lists.htm
#!usr/bin/python3
from utility import *
printDes("Tutorial of Python List operations", """The whole file contains small examples of python list operations""")

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
print("case1: Get single item : listNum[3] = ", listNum[3])
print("case2: Get sub sequence: listNum[1:5] = ", listNum[1:5])
print("case3: Get sub sequence from index: listNum[:5] = ", listNum[:5])
print("case3: Get sub sequence from index: listNum[5:] = ", listNum[5:])
# Update
printDes("Update list item")
print("case1: before update: listRandom: %s" % strList(listRandom))
listRandom[2] = "y"
print("case1: after update: listRandom: %s" % strList(listRandom))
# Delete
printDes("Delete item from List")
print("case1: delete: before delete: listRandom: %s" % strList(listRandom))
del listRandom[2]
print("case1: delete: after delete: listRandom: %s" % strList(listRandom))
# String operations
printDes("Some string operations", "Some basic string ops")
printDes("Length")
print("Length of the %s is " % strList(listOfFriends), len(listOfFriends))
printDes("Membership")
print("Item %s is available in %s :" % ("Laba", strList(listOfFriends)), "Laba" in listOfFriends)
print("Item %s is available in %s :" % ("Mano", strList(listOfFriends)), "Mano" in listOfFriends)
printDes("Repetition")
smallList = [2,7]
print("%s * 3 = " % (smallList), smallList * 3)
# Indexing, Slicing
printDes("Indexing, Slicing", "Same as string")
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
printDes("Some Useful List methods")
# append
newFriend = "BB"
print("1. append: %s appending %s  " % (strList(listOfFriends), newFriend))
listOfFriends.append(newFriend)
print("1. append: Result => ", listOfFriends)
# count
redundantList = ["Mango","Apple", "Banana", "Mango"]
mango = "Mango"
apple = "Apple"
print("2. count: the count of %s in" % mango, redundantList, "is ", redundantList.count(mango))
print("2. count: the count of %s in" % apple, redundantList, "is ", redundantList.count(apple))
# extend
def extendList(l1, l2):
    l1.extend(l2)
    return l1
temp = list(listOfFriends)
print("3. extend:", listOfFriends, ".extend(", redundantList, ") = ", extendList(temp, redundantList))
# index
laba = "Laba"
lele = "Lele"
print("4. index: index of %s in " % laba,listOfFriends, " is ", listOfFriends.index(laba))
print("4. index: index of %s in " % lele,listOfFriends, " is ", listOfFriends.index(lele))
# insert
def insertInList(l, i, v):
    l.insert(i,v)
    return l
blueberry = "Blueberry"
temp = list(redundantList)
print("5. insert: inserting %s at index 2 in " % blueberry,redundantList," => ", insertInList(temp, 2, blueberry))
# pop
temp = list(listRandom)
print("6. pop: poping from ", listRandom," - ",temp.pop()," => ", temp)
# remove
bb = "BB"
def removeFromList(list, item):
    list.remove(item)
    return list
temp = list(listOfFriends)
print("7. remove: removing %s from " % bb,temp," => ", removeFromList(listOfFriends, bb))
# reverse
temp = list(listNum)
temp.reverse()
print("8. reverse: reversing list", listNum, " => ", temp)
# sort
listNum2 = [7,6,1,9,5,3,4,11,0,31]
temp = list(listNum2)
temp.sort()
print("9. sort: ", listNum2, " => ", temp)
temp = list(listOfFriends)
temp.sort()
print("9. sort: ", listOfFriends, " => ", temp)
print("\n\n---- END:LIST ----\n\n")
