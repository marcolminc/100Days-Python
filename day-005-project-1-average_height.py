"""Average Height.

A program that calculates the average student height from a list of heights.

Note:
    not allowed to use: sum(), len()
"""
student_heights = input("Input a list of student heights:\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# write your code below this
total, length = 0, 0
for height in student_heights:
    total += height
    length += 1
avg = int(round(total / length, 0))
print(avg)