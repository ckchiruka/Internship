#!/usr/bin/python3

#Exceptions are an easy to test things in python
try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line)

#Except catches the error, and allows to print it if necessary
except IOError as e:
    print("something bad happened ({})".format(e))

print("after badness")
