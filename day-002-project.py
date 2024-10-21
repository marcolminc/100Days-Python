# num = int(input('write a 2-digit number: '))
# sum_digits = int(num / 10) + (num % 10)
# print('sum of digits is: ' + str(sum_digits))
#
# bmi 1.0
# height = input('enter your height in m: ')
# weight = input('enter your weight in kg: ')
# bmi = int((float(weight)) / (float(height) ** 2))  # ** = exponent operator
# print('your BMI is: ', bmi, sep='')

# your life in weeks
# current_age = input('what is your current age? ')
# age_left = 90 - int(current_age)
# days_left = age_left * 365
# weeks_left = age_left * 52
# months_left = age_left * 12
# print(f"you have {days_left} days, {weeks_left} weeks, and {months_left} months left")


# tip calculator
bill = float(input('enter the bill: $'))
people = int(input('enter number of people to split the bill with: '))
tip = int(input('enter tip percentage: '))
per_person = "{:.2f}".format(round(float((bill / people) * (1 + float(tip / 100))), 2))
print(f"each person should pay ${per_person}")
