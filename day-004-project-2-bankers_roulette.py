"""Who's Paying?

A program that selects a name randomly from the list of names.
The person selected will have to pay for everybody's food bill.

Note:
    Not allowed to use choice()
    splits the string name_string into individual names and puts them inside a list called names.
    All the names are entered, comma and space separated. E.g., name, name, name

Hint:
    use split()
"""
import random

names = input("Give me everybody's names, separated by a comma and a space ', ':\n").split(', ')
print('{:s} is paying today!'.format(names[random.randint(0, len(names) - 1)]))
