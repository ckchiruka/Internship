#!/usr/bin/python3

def main():
    #Strings are immutable objects created with either single or double quotes
    s = "This is a string"
    print(s)
    #Place a \n in the middle of a string to start a newline
    s = "This is a \nstring"
    print(s)
    #Raw string used to create regular expressions, in order to keep \n
    s = r"This is a \nstring"
    print(s)
    #Python 3 way of inserting value of n in string
    #. is an object deferencing operator, to access format method
    n = 42
    s = "This is a {} string".format(n)
    print(s)
    #Python 2 way of inserting value of n in string
    n = 42
    s = "This is a %s string" % n
    print(s)
    #Triple quotes in python, \ escapes the blank line in the beginning
    n = 42
    s = '''\
This is a %s string
Line after line of text
and more text
''' % n
    print(s)

if __name__ == "__main__" : main()
