#!/usr/bin/python3

import re

def main():
    fh = open('raven.txt')
    #search and replace in python
    for line in fh:
        print(re.sub('(Len|Neverm)ore', "###", line), end='')
        #print only lines where search and replace took place
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(line.replace(match.group(), '####'), end = '')
    

if __name__ == "__main__": main()
