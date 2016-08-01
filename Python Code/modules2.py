#!/usr/bin/python3

#pypi.python.org/pypi: repository of software for the python language

import bitstring

def main():
    a = bitstring.Bits(bin = '01010101')
    print(a.hex, a.bin, a.uint)
    

if __name__ == "__main__": main()
