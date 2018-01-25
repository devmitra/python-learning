# File Name learn_json_parsing.py
# Demo for basic JSON parsing tutorial
# link : https://docs.python.org/3.6/library/json.html
#!usr/bin/python3

# Json parser
import json
# Local Utility
from utility import *
printDes("Simple JSON Parsing")

jsonString = """{
    "name" : "Laba",
    "surname": "Ballabh",
    "type": "gandu",
    "work": "gas production",
    "keys": ["besu", "kalyani", "Taki House"]
}"""

jsonObj = json.loads(jsonString) # use load for file input

print("Input JSON:")
print(jsonString)
print("Output JSON Object (%s): " % type(jsonObj))
print(jsonObj)

dictObj = {"name" : "Pungi",
"surname" : "Gupta",
"type" : "dhobbaz",
"work" : "only dhobbaz",
"keys": ["Vidyasagar", "Hare"]}

newJSONStr = json.dumps(dictObj) # use dump for file output

print("Input Dict:")
print(dictObj)
print("JSON String:")
print(newJSONStr)

printEnd()
