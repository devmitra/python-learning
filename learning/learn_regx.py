# File Name learn_regx.py
# Demo for basic Python Regular expression functionality
# link : https://www.tutorialspoint.com/python3/python_reg_expressions.htm
#!usr/bin/python3


import sys
import re
from utility import *
printDes("Regx: Regular Expression", "Regular expression class is used to classify text patterns")

# Flags, Regular Expression Modifier
# *********************
# ASCII, A  => Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.
# DOTALL,S, re.S  => Matches any char including \n
# IGNORECASE, I, re.I => ignore case
# LOCALE, L, re.L => Do a locale-aware match
# MULTILINE, M, re.M => Multi-line matching, affecting ^ and $
# VERBOSE, X (for ‘extended’) => Enable verbose REs, which can be organized more cleanly and
#                                understandably
#   re.X => Permits "cuter" regular expression syntax.
#       It ignores whitespace (except inside a set [] or when escaped by a backslash) and
#       treats unescaped # as a comment marker.
#   re.U => Interprets letters according to the Unicode character set.
#           This flag affects the behavior of \w, \W, \b, \B.

# Patterns
# *********************
# * => 0 or any such group
# Example:
def example1():
    rgx = r'ab*' # => String with a follwed by 0 or more bs
    text1 = "abbbbbb"
    text2 = "a"
    text3 = "b"
    text4 = "abbbbcdabb"
    print("Example1:", text1,"match ", rgx," => ", re.match(rgx, text1, re.M | re.I))
    print("Example1:", text2,"match ", rgx," => ", re.match(rgx, text2, re.M | re.I))
    print("Example1:", text3,"match ", rgx," => ", re.match(rgx, text3, re.M | re.I))
    print("Example1:", text4,"match ", rgx," => ", re.match(rgx, text4, re.M | re.I))
    print("Example1:", text4,"search ", rgx," => ", re.search(rgx, text4, re.M | re.I))
# End: example1
example1()

# + => 1 or any such group
def example2():
    rgx = r'ab+'
    text1 = "abbbbbb"
    text2 = "a"
    text3 = "b"
    text4 = "abbbbcdabb"
    print("Example2:", text1,"match ", rgx," => ", re.match(rgx, text1, re.M | re.I))
    print("Example2:", text2,"match ", rgx," => ", re.match(rgx, text2, re.M | re.I))
    print("Example2:", text3,"match ", rgx," => ", re.match(rgx, text3, re.M | re.I))
# End: example2
example2()

# [^ab] => not started with ab
def example3():
    rgx = r'[^ab]'
    text1 = "abcd"
    text2 = "luke"
    print("Example3:", text1,"match ", rgx," => ", re.match(rgx, text1, re.M | re.I))
    print("Example3:", text2,"match ", rgx," => ", re.match(rgx, text2, re.M | re.I))
# End example3
example3()

# . (periods) => any single char except '\n'
def example4():
    rgx = r'.*'
    text1 = "\n"
    text2 = "gorminit\n"
    print("Example4:", text1,"match ", rgx," => ", re.match(rgx, text1, re.M | re.I))
    print("Example4:", text2,"match ", rgx," => ", re.match(rgx, text2, re.M | re.I))
# End example4
example4()

# ? => optional
def example5():
    rgx = r'abc?'
    text1  = 'abc'
    text2 = 'ab'
    text3 = "abb"
    text4 = "bac"
    print("Example5:", text1,"match ", rgx," => ", re.match(rgx, text1, re.M | re.I))
    print("Example5:", text2,"match ", rgx," => ", re.match(rgx, text2, re.M | re.I))
    print("Example5:", text3,"match ", rgx," => ", re.match(rgx, text3, re.M | re.I))
    print("Example5:", text4,"match ", rgx," => ", re.match(rgx, text4, re.M | re.I))
# End example5
example5()

# {n} => match exactaly 3 instance
# {n,} => match 3 or more
# {n,m} => match m to n
def example6():
    rgx = r'a{2}\w'
    text1 = "aalaba"
    text2 = "ablaba"
    print("Example6:", text1,"match ", rgx," => ", re.match(rgx, text1, re.M | re.I))
    print("Example6:", text2,"match ", rgx," => ", re.match(rgx, text2, re.M | re.I))

    rgx = r'a{2,}\w'
    text1 = "aalaba"
    text2 = "ablaba"
    text3 = "aaalaba"
    print("Example6:", text1,"match ", rgx," => ", re.match(rgx, text1, re.M | re.I))
    print("Example6:", text2,"match ", rgx," => ", re.match(rgx, text2, re.M | re.I))
    print("Example6:", text3,"match ", rgx," => ", re.match(rgx, text3, re.M | re.I))

    rgx = r'a{2,5}\w'
    text1 = "aalaba"
    text2 = "ablaba"
    text3 = "aaaaalaba"
    text4 = "aaaaaaaablaba"
    print("Example6:", text1,"match ", rgx," => ", re.match(rgx, text1, re.M | re.I))
    print("Example6:", text2,"match ", rgx," => ", re.match(rgx, text2, re.M | re.I))
    print("Example6:", text3,"match ", rgx," => ", re.match(rgx, text3, re.M | re.I))
    print("Example6:", text4,"match ", rgx," => ", re.match(rgx, text4, re.M | re.I))

# End example6
example6()

# \w => any word [a-zA-Z0-9]+
# \W => any non word [^a-zA-Z0-9]
# \b => boundary
# \s => whitespace, newline, \r
# \S => non whitespace
# \t, \n, \r
# \d => any digit [0-9]+
# \D => [^0-9]+
# ^ => Start of strings
# $ => End of strings
# \ => inhibit the "specialness" of a character.
# re.escape(str) => to create regx from string
