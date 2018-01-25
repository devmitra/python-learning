# File Name learn_xml_parsing.py
# Demo for basic xml parsing tutorial
# link : https://docs.python.org/3.6/library/xml.etree.elementtree.html
#!usr/bin/python3

# XML Parser
import xml.etree.ElementTree as ET
# Local Utility
from utility import *

printDes("Simple XML Parsing")

xmlVal = "<data type='pure gandu'>LABA</data>"
root = ET.fromstring(xmlVal)
print("ROOT:", root.tag)
print("VALUE:", root.text)
print("ATTRIBUTE:", root.attrib)

tree =  ET.parse("./data/test.xml")
root = tree.getroot()

# Function: printTag
def printTag(root):
    print(root.tag, "== Startn ==")
    print("value: ", root.text)
    print("Attribute:", root.attrib)
    for child in root:
        printTag(child)
    #   end-for
    print(root.tag, "== End ==")
#   end [printTag]
# Printing
printTag(root=root)

# Non blocking Parser
printDes("Non blocking Pull Parser")
fileData = open('./data/test.xml').read()

def pullParse(data):
    parser = ET.XMLPullParser(['start','end'])
    parser.feed(data)
    for event, elem in parser.read_events():
        print('Event: ', event)
        if elem.text != None:
            text = elem.text.replace('\n','')
            text = text.replace(' ','')
            if text != '':
                print('Tag:', elem.tag, ", text:", elem.text)
            else:
                print('Tag:', elem.tag, ", text: NONE")


    #   [end-for]
#   end [pullParse]
pullParse(fileData)

sample = '<sona><luck>Sample</luck>'
pullParse(sample)



#print(list(parser.read_events()))
