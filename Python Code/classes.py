#!/usr/bin/python3

class Egg:
    def __init__(self, kind = "fried"):
        self.kind = kind #creates an object variable, each instance is different

    def whatKind(self):
        return self.kind

def main():
    #object is an instance of a class
    fried = Egg() # uses default value, constructor called everytime
    scrambled = Egg('scrambled') #uses given value, constructor still called
    print(fried.whatKind())
    print(scrambled.whatKind())


if __name__ == "__main__" : main()
