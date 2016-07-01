#!/usr/bin/python3

def main():
    for n in testfunc(): print(n, end = ' ')

def testfunc():
    #return keyword is how values are returned, and can be anytype
    return range(25)

if __name__ == "__main__": main()
