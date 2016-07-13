#!/usr/bin/python3

#tuples created with comma operator
t = 1, 2, 3, 4, 5
print(t)
print(t[1])
print(t[-1])
print(len(t), min(t), max(t))
#create a tuple with 1 element
onet = (1,)
print(type(onet))
#lists are created with square brackets
lst = [1, 2, 3, 4, 5]
print(lst, type(lst), lst[0], lst[-1], min(lst), max(lst))
tup = tuple(range(25))
#tuples cannot be changed, are immutable
lst = list(range(25))
print(lst)
lst[10] = 42
print(lst)

