#!/usr/bin/python3

t = tuple(range(25))
print(t, type(t))
print( 10 in t, 50 in t, 50 not in t, len(t))
for i in t: print(i)

l = list(range(20))
print(10 in l, 20 in l, 20 not in l, len(l))
for i in l: print(l)
l[10] = 25
print(l)

print(t.count(5), t.index(5))
l.append(100)
print(len(l), l)
l.extend(range(20))
print(len(l), l)
l.insert(0, 25)
print(len(l), l)
l.insert(12, 100)
print(len(l), l)
l.remove(12)
print(len(l), l)
del l[12]
print(len(l), l)
print(l.pop())
print(len(l), l)
print(l.pop(0))
print(len(l), l)



