"""A virtual coin toss program.

It randomly tells the user 'Heads' or 'Tails'.
"""

import random

toss = random.randint(0, 1)
print('Heads' if toss else 'Tails')

