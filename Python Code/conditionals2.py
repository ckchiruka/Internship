#!/usr/bin/python

def main():
    #regular conditional statements in python
    a, b = 1, 1
    if a < b:
        print("a is less than b")
    elif  a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")

    #the conditional expression in python
    a, b = 1, 1
    s = "less than" if a < b else "not less than"
    print(s)

    

if __name__ == "__main__": main()
