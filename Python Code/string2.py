#!/usr/bin/python3

s = 'This is a string'
print(s)
print(s.upper())
print('This is a string'.upper())
print('This is a string {}'.format(42))
print('This is a string %d' % 42)
t = 'this is a string'
print(t)
print(t.capitalize())
print(t.upper())
print(s.lower())
print('THIS IS A STRING'.lower())
print('THis IS a StRing'.swapcase())
print(s.find('is'))
print(s.replace('this', 'that'))
print('      This is a string    '.strip())
print('      This is a string    '.rstrip())
s1 = 'This is a string\n'
print(s1)
print(s1.strip())
print(s1.rstrip('\n'))
#returns true is all characters are alphanumeric
print(s.isalnum())
print('thisisastring'.isalnum())
print('thisisastring'.isalpha())
print('12349208545435'.isdigit())
print(s.isdigit())
print(s.isprintable())
a, b = 5, 42
print(a, b)
print('this is {}, that is{}'.format(a,b))
s = 'this is {}, that is{}'
print(s)
print(s.format(a,b))
print(id(s))
new = s.format(a,b)
#format returns a new string with different id
print(id(new))
#format method doesn't need to know type of variable
print('this is %d, that is %d' % (a,b))
#can specify positional arguments in curly brackets and name them
print('this is {1}, that is{0}'.format(b,a))
print('this is {1}, and that is {0}, and this too is {1}'.format(a,b))
print('this is {bob}, that is {fred}'.format(bob = a, fred = b))
d = dict(bob = a, fred = b)
print('this is {bob}, that is {fred}'.format(**d))

r = 'This is a string of words'
print(r)
print(r.split())
print('this     is      a    string   of     words'.split())
print(r.split('i'))
words = r.split()
print(words)
for w in words: print(w)
new = ':'.join(words)
print(new)
print(', '.join(words))








      
