"""
Today I learned about:
- string basic string manipulation
- taking string (user) input using print()
- single line commenting
- docstring
- finding length of string (number of its characters
- variables
"""
print("Day 1 = String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello" + "world")')
print("New lines can be created with a backslash and n.")
# asks for your name then prints `hello __your_name`
# print('Hello ' + input('what is your name? '))

# prints the number of characters in a user's name (input)
print('number of characters:', len(input('what is your name? ')), sep=' ')

name = input('where do you come from?')
