#!/usr/bin/python3

class Duck:
    #these are methods to the class duck
    #self variable is a reference to the object
    #and everything attached to the object
    #constructor method, common purposes are to initialize data
    def __init__(self, value):
        self._v = value
    #_v can be used in other methods as well     
    def quack(self):
        print("Quaaaaaaaaaack!", self._v)
        
    def walk(self):
        print("Walks like a duck.", self._v)

#methods are functions that are attributes of an object
def main():
    donald = Duck(47)
    frank = Duck(515)
    donald.quack()
    donald.walk()
    #value is attached to the object not to the class, encapsulation
    frank.quack()
    frank.walk()

if __name__ == "__main__": main()
