# File Name learn_function.py
# Demo for basic Python tuple functionality
# link : https://www.tutorialspoint.com/python3/python_functions.htm
#!usr/bin/python3

from utility import *
printDes("Functions", "This tutorial explains, how to use function and lambda function in python")

# Function
def laba(str):
    print("Hi, I am Laba: and my received input as argument is => ", str)
    return 1

ret = laba("Gas Ballabh")
print("Return value of laba = ", ret)

# Function with multiple argument
def gas(arg1, arg2):
    print("Gas: argument 1 is => ", arg1)
    print("Gas: argument 2 is => ", arg2)


# Calling method
gas("pungi", "lungi")

# Calling gas with keyword argument
gas(arg2 = "GULAL", arg1="Modu")

# Fuction with default arg
def BAAP(member = "Babin"):
    print("BAAP(Boro Loker Aalida Pola community): the member: ", member)

# Calling with default argument
BAAP()
# Calling with argument
BAAP("Samrat")

# Variable length argument
def BAAP_V2(top = "Babin", *others):
    print("BAAP(Boro Loker Aalida Pola community): Top position belong to => ", top)
    print("BAAP(Boro Loker Aalida Pola community): Other members => ", others)

BAAP_V2("Babin", "Abhra", "Samrat", "Subhra")
BAAP_V2("Pungi", "Kutta")
BAAP_V2()
BAAP_V2(0,"Abhra", "Laba")

# Lambda function: Inline function
listItem = []
puneRegroup = lambda item, member: item.append(member)

itm = puneRegroup(listItem,"Guzarish")
itm = puneRegroup(listItem,"Gulal")
itm = puneRegroup(listItem,"Sir")
itm = puneRegroup(listItem, "Chiru")
itm = puneRegroup(listItem,"Bunip")
itm = puneRegroup(listItem,"Teko")
itm = puneRegroup(listItem, "Maggi")

print("puneRegroup = ", listItem)


printEnd()
