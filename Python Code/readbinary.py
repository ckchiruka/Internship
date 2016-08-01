#!/usr/bin/python3

def main():
    #'rb' = read binary
    buffersize = 50000
    infile = open('olives.jpg', 'rb')
    outfile = open('binary.jpg', 'wb')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end = '')
        buffer = infile.read(buffersize)
    print('\nDone')
    
if __name__ == "__main__": main()
