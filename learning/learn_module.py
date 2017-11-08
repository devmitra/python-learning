# File Name learn_module.py
# Demo for basic logic of python module
# link : https://www.tutorialspoint.com/python3/python_modules.htm
#!usr/bin/python3

from utility import *

# Need to append package path to sys. So it can load modules from the package dir.
import sys
sys.path.append("./testModule")

# Importing a package as module: Check structure of testModule dir. __init__.py
# acts as index for all modules in dir.
import testModule


printDes("Tutorial for python module concept")

# Global keyword
greetings = "Hello, "
def labaGreets(person):
    global greetings
    return greetings + person + ", I am Laba, have a niceday!"

print(labaGreets("Kutta"))

# Using testModule function
testModule.Test1()

printEnd()
