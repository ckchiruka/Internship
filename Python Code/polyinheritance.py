#!/usr/bin/python3
#Inheritance and Polymorphism
#Classes Duck, Person, and Dog inherit their functions(quack, feathers, bark
# and fur) from AnimalActions
class AnimalActions:
    def quack(self): return self.string['quack']
    def feathers(self): return self.string['feathers']
    def bark(self): return self.string['bark']
    def fur(self): return self.string['fur']

class Duck(AnimalActions):
    string = dict(
        quack = "Quaaaak!",
        feathers = "The duck has gray and white feathers.",
        bark = "The duck cannot bark.",
        fur = "The duck has no fur."
        )

class Person(AnimalActions):
    string = dict(
        quack = "The person imitates a duck.",
        feathers = "The person takes a feather from the ground and shows it.",
        bark = "The person says woof!",
        fur = "The person puts on a fur coat."
        )

class Dog(AnimalActions):
    string = dict(
        quack = "The dog cannot quack.",
        feathers = "The dog has no feathers.",
        bark = "Arf!",
        fur = "The dog has white fur with black spots."
        )

#Polymorphism thru the class, since all of Person, Dog, and Duck have the same
#functions, allowing one function to call the same thing, but have different
#consequences
def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())

def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())

def main():
    donald = Duck()
    john = Person()
    fido = Dog()

    print("- In the forest:")
    for o in (donald, john, fido):
        in_the_forest(o)

    print("- In the doghouse:")
    for o in (donald, john, fido):
        in_the_doghouse(o)

if __name__ == "__main__": main()

    
