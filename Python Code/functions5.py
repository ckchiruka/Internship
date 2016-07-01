#!/usr/bin/python3

def main():
    #passing in keyword arguements
    #arguements must be in this order: named, tuple, keyword
    testfunc(5, 6, 7, 8, 9, 10, one = 1, two = 2, four = 42)

#**kwargs are the keyword arguements stored in a dictionary
def testfunc(this, that, other, *args, **kwargs):
    print('This is a test function',
          this, that, other, args,
          kwargs['one'], kwargs['two'], kwargs['four'])
    #keyword args
    for k in kwargs: print(k, kwargs[k])
    #tuple args
    for n in args: print(n)

if __name__ == "__main__": main()
