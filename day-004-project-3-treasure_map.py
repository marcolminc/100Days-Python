"""Treasure map.

Use Lists(nested) and indexing to place an x(the treasure) on a specific position on the matrix.
the user should input two-digit number where the first digit is for the column and the second for the row.
"""

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
position = input('where do you want to put the treasure? ')
# position = int(position)
# col = position // 10
# row = position % 10
row = int(position[1])
col = int(position[0])
map[row - 1][col - 1] = 'x'
print(f'{row1}\n{row2}\n{row3}')


