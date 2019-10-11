# File Name learn_lambda.py
# Demo for Python collection function like map, filter, sort with lambda
# link :
#!usr/bin/python3

from utility import *

# map
numList = [1,2,3,12,67]
numList1 = [56,78,15,79, 87, 65, 4, 8,19, 101, 21, 68, 45, 89]

tagMap = {1 : "Laba", 2: "Pungi", 3: "Lej", 12: "Hondo"}

# cube: list cube with lambda expression
def cube(l):
    return list(map(lambda x: x**3, l))
# end-cube

# add5: add 5 with num
def findTag(l):
    def tag(x):
        return (x, tagMap.get(x, "No Tag"))
    return list(map(tag,l))

print("cube(", numList, ") => ", cube(numList))
print("findTag(", numList, ") => ", findTag(numList))

# filter
ranSeq = randomSeq(10)
print("Random Sequence: ",ranSeq, ", filtering x > 500:", list(filter(lambda x: x > 500, ranSeq)))
print("Random Sequence: ",ranSeq, ", filtering x < 500:", list(filter(lambda x: x < 500, ranSeq)))

printEnd()
