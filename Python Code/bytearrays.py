#!/usr/bin/python3

def main():
    #bytes and byte arrays contain bytes or 8-bit words of data
    #8-bits can hold up to 256 values, and it convenient for converting strings
    #tells python to use utf 8 encoding system
    fin = open('utf8.txt', 'r', encoding = 'utf_8')
    #makes an html file
    fout= open('utf8.html', 'w')
    #creating bytearray
    outbytes = bytearray()
    #gets line
    for line in fin:
        #gets characters
        for c in line:
            #if character is 128+, its a special character so we encode using
            #utf8 and add onto end of outbytes
            if ord(c) > 127:
                outbytes += bytes('&#{:04d};'.format(ord(c)), encoding = 'utf_8')
            #else its a regular character and add onto beginning of outbytes
            else: outbytes.append(ord(c))
    #create the string we want to print
    outstring = str(outbytes, encoding = 'utf_8')
    print(outstring, file = fout)
    print(outstring)
    print('Done.')
    #bytearrays allow you to operate on character data
if __name__ == "__main__": main()
