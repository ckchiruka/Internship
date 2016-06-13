#!/usr/bin/python

def main():
    func(1)
    func() #default argument
    func(5)

#defining a simple function
def func(a = 7): #default argument starts at 7
    for i in range(a, 10):
        print(i, end=' ')
    print()


if __name__ == "__main__": main()
