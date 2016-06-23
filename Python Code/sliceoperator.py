#!/usr/bin/python3

def main():
    list = []
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #ranges in python are noninclusice, so list[5]s will not be printed
    print(list[0:5])
    #creates list from 0 to 99
    list[:] = range(100)
    print(list)
    #list from 27 to 41
    print(list[27:42])
    #list from 27 to 41 by step 3
    print(list[27:42:3])
    #creates iterator, so you can use for loops
    for i in list[27:43:3] : print(i)
    #lists are mutable
    list[27:43:3] = (99, 99, 99, 99, 99, 99)
    print(list)

if __name__ == "__main__": main()
