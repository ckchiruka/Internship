#!/usr/bin/python3

#regular function
def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

#generator function, because of yield
def primes(n = 1):
    while(True):
        #Yield returns a number only if isprime returns true
        #next time yield is called it start at n + 1
        if isprime(n): yield(n)
        n += 1
        
#use of generator function as an iterator, and allows for use of for loop
for n in primes():              
    if n > 100: break          
    print(n)
