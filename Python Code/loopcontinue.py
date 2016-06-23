#!/usr/bin/python

def main():
    s = 'this is a string'
    #continue shortcuts the loop and goes back to the beginning
    for c in s:
        if c == 's' : continue
        print(c, end ='')
    #else get runs whenever iterator is out of stuff to iterate
    #else also works in while loop
    else:
        print("else")
    #break jumps out of a loop
    for c in s:
        if c == 's' : break
        print(c, end ='')
        


if __name__ == "__main__": main()
