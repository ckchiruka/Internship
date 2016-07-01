#!/usr/bin/python3

def main():
    
    try:
        fh = open('xlines.txt')
        #if you have more than one line in try, it stops once error gets raised
        for line in fh: print(line.strip())
    except IOError as e:
        print("Could not open the file:", e)
        
if __name__ == "__main__" : main()
