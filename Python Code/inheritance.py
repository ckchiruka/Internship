#!/usr/bin/python3

class Animal:
    def talk(self):
        print('I have something to say')
    def walk(self):
        print("Hey! I'm walking here")
    def clothes(self):
        print("I have nice clothes")      

#duck now inherits all of the methods in animal
class Duck(Animal):
    def quack(self):
        print("Quaaaaaaaaaack!")
    def walk(self):
        #super() allows parent classes' methods to use run in the child
        super().walk()
        print("Walks like a duck.")

class Dog(Animal):
    def clothes(self):
        print("I have brown and white fur")

def main():
    donald = Duck()
    donald.quack()
    #walk in duck overrides walk in animal when not using super()
    donald.walk()
    donald.clothes()

    fido = Dog()
    fido.walk()
    fido.clothes()

if __name__ == "__main__": main()
