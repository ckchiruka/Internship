#!/usr/bin/python3

#create dictionary with curly brackets
d = {'one': 1, 'two': 2, 'three': 3}
#easier way to create dictionary
d = dict(one = 1, two = 2, three = 3)
print(d, type(d))
x = dict(four = 4, five = 5, six = 6)
print(x)
d = dict(**d, **x)
print(d)
print('four' in x, 'nine' not in d)
for k,v in d.items(): print(k,v)
print(x.get('three', 'not found'), d.get('three'))
del x['four']
print(x.pop('five'))
print(x)
