#!/usr/bin/python3

import sys

#While Loops in python
a, b = 0, 1
while b < 50:
    print(b)
    a, b = b, a + b
#No paranthesis needed to end loops
print("Done")

#For Loops in python
fh = open('lines.txt')
#Disclaimer readline() is different than readlines()
for line in fh.readlines():
    #All print functions have newline builtin, specify if no newline in needed
    print(line, end="")
    
