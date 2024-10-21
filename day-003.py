# conditional statements, nested conditional statements
height = float(input('what is your height in cm? '))
if height >= 120.00:
    age = int(input('how old are you? '))
    if age <= 18:
        print('pay $7 please.')
    else:
        print('pay $18 please.')
else:
    print('grow tall...')