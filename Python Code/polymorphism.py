#!/usr/bin/python3

class Duck:
    def quack(self):
        print("Quaaaaaaaaaack!")
    def walk(self):
        print("Walks like a duck.")
    def bark(self):
        print("The duck cannot bark")
    def fur(self):
        print("The duck has feathers")

class Dog:
    def bark(self):
        print('Woof!')
    def fur(self):
        print("The dog has brown and white fur")
    def walk(self):
        print("Walks like a dog")
    def quack(self):
        print("The dog cannot quack")

def main():
    donald = Duck()
    fido = Dog()
    #objects in python don't care what the name of a class is
    #python is duck typing, its loosely typed
    #any object of any class that implements the interface that's expected
    #by any function can be used by that function
    in_the_forest(donald)
    in_the_pond(fido)
    
def in_the_forest(cat):
    cat.bark()
    cat.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()

if __name__ == "__main__": main()
