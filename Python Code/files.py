#!/usr/bin/python3

def main():
    #'r' = read, 'rb' = read binary, 'rt' = read text
    #'w' = write, 'r+' = read and write
    #'a' = append
    #open defaults to 'r'
    infile = open('lines.txt', 'r')
    outfile = open('new.txt', 'w')
    for line in infile:
        print(line, file = outfile, end = '')
    print('Done')

    #read files in a couple of big chunks
    #deal with bigger chunks of files, instead of line by line
    buffersize = 50000
    infile = open('bigfile.txt', 'r')
    outfile = open('new1.txt', 'w')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end = '')
        buffer = infile.read(buffersize)
    print('Done.')

if __name__ == "__main__": main()
