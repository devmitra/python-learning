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

    #print("\n")
    return
def strList(list, sep = " "):
    #return "".join('{}'.format(k) for k in list).join(sep)
    res = "[ "
    for k in list:
        res = res + "".join('{}'.format(k)) + sep
    return res + "]"

def printEnd():
    printDes("END")
##############################################################
