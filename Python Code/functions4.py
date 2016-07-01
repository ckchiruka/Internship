#!/usr/bin/python3

def main():
    testfunc(1, 2, 3, 42, 43, 45, 46)

#asterisk is special, since it allows for any number of optional arguments
def testfunc(this, that, other, *args):
    print(this, that, other)
    #args gives us a tuple, which is immutable
    for n in args: print(n, end = ' ')

if __name__ == "__main__": main()
