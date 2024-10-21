"""Rock, Paper, Scissors game.
"""

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]
player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n'))
if player_choice < 0 or player_choice > 2:
    print('Wrong choice, expected (0, 1 or 2)')
    exit()
print(f'your choice:\n{choices[player_choice]}')
comp_choice = random.randint(0, 2)
print(f'computer choice:\n{choices[comp_choice]}')

if (
        (choices[player_choice] == rock and choices[comp_choice] == scissors) or
        (choices[player_choice] == scissors and choices[comp_choice] == paper) or
        (choices[player_choice] == paper and choices[comp_choice] == rock)
):
    print('You Win!')
elif player_choice == comp_choice:
    print('It\'s a draw.')
else:
    print('You lose.')
