#!/usr/bin/python3

import re

def main():
    fh = open('raven.txt')
    #more efficient since we're compiling the regex once, instead of each time
    #a number of efficiencies are available with re.compile
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(line, end = '')
            print(pattern.sub('###', line), end = '')


if __name__ == "__main__": main()
