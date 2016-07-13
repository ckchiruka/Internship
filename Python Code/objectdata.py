#!/usr/bin/python3

class Duck:
    def __init__(self, **kwargs):
        #_attributes are used locally and not directly
        #all access is done within method inside the object
        self.variables = kwargs
    def quack(self):
        print("Quaaaaaaaaaack!")
    def walk(self):
        print("Walks like a duck.")
    #dicionary objects allow for a lot of flexibility with different data
    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)

def main():
    donald = Duck(feet = 2)
    #code itself has control over what happens
    #using accessor methods is a standard, in order to maintain control over data
    donald.set_variable('color', 'blue')
    print(donald.get_variable('feet'))
    print(donald.get_variable('color'))

if __name__ == "__main__": main()
