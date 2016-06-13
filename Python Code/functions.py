#!/usr/bin/python3

#How to create a function in python
def isprime(n):
    if n == 1:
        print("1 is special")
        return False
    for x in range(2, n):
        if n % x == 0:
            #Integer division uses two slashs (//)
            print("{} equals {} x {}".format(n, x, n//x))
            return False
    else:
        print(n, "is a prime number")

#Range function only goes thru n-1, in this case 19
for n in range(1, 20):
    isprime(n)

