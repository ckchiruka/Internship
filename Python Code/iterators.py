#!/usr/bin/python3

def main():
    fh = open('lines.txt')
    #enumerate returns two values: an index, and the value from iterator
    for index, line in enumerate(fh.readlines()):
        print(index, line, end='')

    s = 'this is a string'
    #just want the letter s
    for i, c in enumerate(s):
        if c == 's': print('index {} is an s'.format(i))

if __name__ == "__main__": main()
