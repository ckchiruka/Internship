#!/usr/bin/python3

def main():
    #python has no switch function, so dictionaries is a good replacement
    #or just use if/elif/else statements
    choices = dict(
        one = 'first',
        two = 'second',
        three = 'third',
        four = 'fourth',
        five = 'fifth')
    v = 'seven'
    print(choices.get(v, 'other'))


if __name__ == "__main__": main()
