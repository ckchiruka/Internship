#!/usr/bin/python3

def main():
    #tuple is immutable, and created in paranthesis
    #can't change after created, faster than mutable list
    x = (1, 2, 3)
    print(type(x), x)
    #list created with square brackets, is mutable
    x = [1, 2, 3]
    x.append(5)
    x.insert(2,7)
    print(type(x), x)
    #string is also a sequence
    x = 'string'
    #in python, slices don't return the last element, so no 'n'
    print(type(x), x[2:4])
    #all of the sequence types can be used as an iterator
    x = (1, 2, 3, 4, 5)
    for i in x:
        print(i, end = ' ')
    #same with strings
    x = 'string'
    for i in x:
        print(i, end = ' ')

if __name__ == "__main__" : main()
