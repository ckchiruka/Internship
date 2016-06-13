#!/usr/bin/python3

def main():
    num = 42                #regular int
    print(type(num), num)   
    num = 42.0              #regular float
    print(type(num), num)
    num = 42 / 9            #float division
    print(type(num), num)
    num = 42 // 9           #integer division
    print(type(num), num)
    num = round(42 / 9)     #rounding int
    print(type(num), num)
    num = round(42 / 9, 2)  #rouding float
    print(type(num), num)
    num = 42 % 9            #modulo
    print(type(num), num)
    num = int(42.9)         #convert to int
    print(type(num), num)
    num = float(42)         #convert to float
    print(type(num), num)

if __name__ == "__main__" : main()



