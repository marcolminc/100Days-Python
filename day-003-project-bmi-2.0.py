# bmi 2.0
height = input('enter your height in m: ')
weight = input('enter your weight in kg: ')
bmi = int((float(weight)) / (float(height) ** 2))  # ** = exponent operator
status = 'undefined'
if bmi < 18.5:
    status = 'are underweight'
elif 18.5 <= bmi < 25:
    status = 'have normal weight'
elif 25 <= bmi < 30:
    status = 'are overweight'
elif 30 <= bmi < 35:
    status = 'are obese'
else:
    status = 'are clinically obese'
print('your BMI is: ', bmi, ', you ', status, sep='')
