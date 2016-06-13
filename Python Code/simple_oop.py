#!/usr/bin/python3

#simple fibonacci series
#the sum of two elements defines the next set
class Fibonacci():
    #init as 2 underscores on both sides, is a constructor
    #first argument is always self
    #self is a reference to the instantiated object
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #another generator
    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b

#creating an instance of class Fibonacci
f = Fibonacci(0,1)
for r in f.series():
    if r > 100: break
    #print yields from generator
    print(r, end = ' ')
