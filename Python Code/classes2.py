#!/usr/bin/python3

class Duck:
    def quack(self):
        print("Quaaaaaaaaaack!")
    def walk(self):
        print("Walks like a duck.")

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == "__main__": main()
