#!/usr/bin/python3

def main():
    x, y = 0x55, 0xaa
    #print bits function in python
    def b(n):
        print('{:08b}'.format(n))
    b(x)
    b(y)
    #bitwise and, if x and y and 1 output is 1, otherwise 0
    b(x | y)
    #bitwise or, if x and y are 0 output is 0, otherwise 1
    b(x & y)
    #bitwise op for xor, if x and y are same output is 0, otherwise 1
    b(x ^ y)
    b(x ^ 0)
    b(x ^ 0xff)
    #bitwise shift right by y places, same as //ing x by 2**y
    b(x >> 4)
    #bitwise shift left by  place (new bits added are 0s)
    #same as multiplying x by 2**y
    b(x << 4)
    #bitwise complement, switches each 0 and 1 to other one
    #same as -x - 1
    b(~x)


if __name__ == "__main__": main()
