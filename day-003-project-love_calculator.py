print('Welcome to the Love Calculator')
name1 = input('What is your name?\n').lower()
name2 = input('What is their name?\n').lower()
name_str = name1 + name2
# check number of times the letters in the word TRUE occurs in each name
# check number of times the letters in the world LOVE occur in each name
# combine the above numbers to make a 2-digit number
# for love score less than 10 or greater than 90 -> your score is x, you go together like coke and mentos
# for love score between 40 and 50 -> your score is y, you are alright together
# otherwise just the score: your score is z
# use tolower() and count() - count makes no repetition when counting occurences of a letter (substr)
# concatenate the names into a single string

true_count = 0
love_count = 0
true_count += name_str.count('t')
true_count += name_str.count('r')
true_count += name_str.count('u')
true_count += name_str.count('e')

love_count += name_str.count('l')
love_count += name_str.count('o')
love_count += name_str.count('v')
love_count += name_str.count('e')
# for letter in name1:
#     if letter in 'TRUE' or letter in 'true':
#         true_count += 1
#     if letter in 'LOVE' or letter in 'LOVE':
#         love_count += 1
# for letter in name2:
#     if letter in 'TRUE' or letter in 'true':
#         true_count += 1
#     if letter in 'LOVE' or letter in 'LOVE':
#         love_count += 1
percent_string = str(true_count) + str(love_count)
percent_value = int(percent_string)
if percent_value < 10 or percent_value > 90:
    print(f"your score is {percent_value}, you go together like coke and mentos")
elif 40 < percent_value < 50:
    print(f"your score is {percent_value}, you are alright together")
else:
    print(f"Your score is {percent_value}")

