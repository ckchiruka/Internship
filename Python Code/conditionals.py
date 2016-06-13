#!/usr/bin/python3

#In python, you can assign multiple values at a time
a, b = 5, 1
#Regular if/else, one thing to note is the semicolon and no paranthesis
if a < b:
    #Using print you can replace numbers and strings using {} and .format()
    print('a ({}) is less than b ({})'.format(a,b))
else:
    print('a ({}) is not less than b ({})'.format(a,b))

#Python has conditional expressions ie print( a < b ? "foo" : "bar"
print("foo" if a < b else "bar")
