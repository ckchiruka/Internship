#!/usr/bin/python3

def main():
    print("This is the functions.py file.")
    for i in inclusiveRange():
        print(i, end = ' ')

def inclusiveRange(*args):
    numargs = len(args)
    #making inclusiveRange work like range works,
    #does exactly what range does except it is inclusive
    if numargs < 1: raise TypeError('requires at least one arguement')
    elif numargs == 1:
        start, stop, step = 0, args[0], 1
    elif numargs == 2:
        start, stop, step = args[0], args[1], 1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError('inclusiveRange expected at most 3 arguments, got {}'
                          .format(numargs))
    i = start
    while i <= stop:
        #each time yield is run, it returns i and execution conties right after yield statement
        #yield turns function into a generator, which generates an interator object
        yield i
        i += step
    

if __name__ == "__main__": main()
