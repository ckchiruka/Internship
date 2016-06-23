#!/usr/bin/python3

def main():
    #create dictionary using curly brackets, and assign a string to each
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    #prints in no particular order
    print(d)
    #using builtin generator to loop, sorted alphabetically by keys
    for k in sorted(d.keys()):
        print(k, d[k])
    #keyword arguments
    d = dict(one = 1, two = 2, three = 3, four = 4, five = 'five')
    #dictionaries are mutable
    d['seven'] = 7
    print(d)

if __name__ == "__main__" : main()
