# File Name similar-string.py
# Problem Statement
#!usr/bin/python3

# IMPORT
import sys
# Method: similar
def similar(s1, s2):
    print("--------------------")
    print("s1 = %s s2=%s" % (s1,s2))
    if s1 == s2:
        print("s1=%s s2=%s = TRUE(1)" % (s1,s2))
        return True
    if len(s1) == len(s2):
        length = len(s1)
        similarFlag = True
        for i in range(0, length):
            for j in range(i, length):
                if i != j:
                    print(s1[i],",",s1[j],","," <=> ",s2[i],",",s2[j])
                    if (s1[i] == s1[j] and s2[i] == s2[j]) or (s1[i] != s1[j] and s2[i] != s2[j]):
                        similarFlag = True
                    else:
                        print("pair = ", i, ",",j)
                        similarFlag = False
                        break
                    # end-if-else
            # end-for-inner
            if not similarFlag:
                break
            # end-if
        # end-for-outer
        print("s1=%s s2=%s = " % (s1,s2), similarFlag)
        return similarFlag
    else:
        print("s1=%s s2=%s = FALSE(1)" % (s1,s2))
        return False
# end-similar

# SubString
def substrings(inputStr, length):
    ipLen = len(inputStr)
    #print("Input = %s ip Len: %d len = %d " % (inputStr,ipLen, length))
    if ipLen == length:
        return [inputStr]
    elif ipLen >= length:
        result = list([])
        bound = (ipLen - length)
        for i in range(0, bound + 1):
            substr = inputStr[i:(i + length)]
            #print("i = %d l = %d bound = %d substr = %s" % (i, i + length, bound, substr))
            result.append(substr)

        return result
    else:
        return []
# end-substrings
# Method: Find Similar substring
def findSimilarSubStr(input,lb, ub):
    ipLen = len(input)
    if lb < 0 and ub > ipLen and lb < ub:
        return (input, [])
    length = ub - lb
    strings = substrings(input, length)
    #print(" strings = ", strings)
    stringSet = set(strings)
    #print("set = ", stringSet)
    strings = list(stringSet)
    #print("strings = ", strings)
    result = list([])
    substring = input[lb:ub]
    #strings.remove(substring)
    result.append(substring)
    for item in strings:
        if item not in result:
            if similar(substring, item):
                result.append(item)
            # end-if
        # end-if
    # end-for
    return (substring, result)
# end-findSimilarSubStr
# Testing
#print("Similar = ", similar("aaa", "bbi"))
#print("substrings: ", substrings("aabcd", 4))
def getConsoleInput(msg):
    condition = True
    stringValue = None
    while condition:
        stringValue = input("%s: " % msg)
        confirm = input("You have entered \"%s\". Is that correct? (y/n): " % (stringValue))
        if confirm == "y" or confirm == "Y":
            condition = False
        # end-if
    # end-while
    return stringValue
# end-getConsoleInput
def app():
    inputStr = None
    lb = -1
    ub = lb
    def getInputs():
        #global inputStr, lb, ub
        inputStr = getConsoleInput("Please enter input string")
        lb = int(getConsoleInput("Please enter lower bound(int)"))
        ub = int(getConsoleInput("Please enter upper bound(int)"))
        return (inputStr, lb, ub)
    # end-getInputs
    condition = True
    inputStatus = False
    while condition:
        ip = getInputs()
        inputStr = ip[0]
        lb = int(ip[1])
        ub = int(ip[2])
        strLen = len(inputStr)
        print("IP => %s(%d) %d %d" % (inputStr, strLen, lb, ub))
        if strLen > 0 and lb >= 0 and ub > lb and ub <= strLen:
            condition = False
            inputStatus = True
            print("Valid INPUT :)")
        else:
            choice = input("You have entered a wrong input do you want to re-enter? (y/n): ")
            if choice == "n" or choice == "N":
                print("Goodbye")
                condition = False
            # end-if
        # end if-else
    # end-while
    if inputStatus:
        result = findSimilarSubStr(inputStr, lb, ub)
        similarList = result[1]
        if len(similarList) > 1:
            print("Similar Strings of %s are " % result[0], similarList)
        else:
            print("No Similar strings of ", result[0])
        # end-if-else
    # end-if
# end-app
# test input str : giggabaj
app()
