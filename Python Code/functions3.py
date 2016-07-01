#!/usr/bin/python3

#main is also a function
#so it can use things that comes after it
def main():
    testfunc(22)

#all function arguments must be initializes in one way or another
#or you can give it the value none
#none is a special value that you can test for
def testfunc(number = 45, another = None, onemore = 75):
    if another is None:
        another = 112
    print('This is a test function', number, another, onemore)
    #basically a no op, pass is a placeholder/stub doesn't do anything
    pass

if __name__ == "__main__": main()
