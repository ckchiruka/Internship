#!/usr/bin/python3

def main():
    try:
        for line in readfile('xlines.doc'): print(line.strip())
    except IOError as e:
        print('cannot read file:', e)
    #print instructions for raised exception
    except ValueError as e:
        print('bad filename', e)

def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    #how to raise an exception in python
    else: raise ValueError('Filename must end with .txt')

if __name__ == "__main__": main()
    
