print('Welcome to Python pizza Deliveries!')
while True:
    size = input('What size of pizza do you want?\n1. small = S\n2. medium = M\n3. large = L:\nchoice: ')
    add_pepperoni = input('Do you want pepperoni?\n1.Yes = Y\n2. No = N\n choice: ')
    extra_cheese = input('Do you want extra cheese?\n1.Yes = Y\n2. No = N\n choice: ')
    bill = 0
    small_pizza = 15
    medium_pizza = 20
    large_pizza = 25
    # pepperoni for small pizza = $2
    # pepperoni for medium/large pizza = $3
    # extra cheese = $1
    if size == 'S':
        bill += small_pizza
    elif size == 'M':
        bill += medium_pizza
    elif size == 'L':
        bill += large_pizza
    else:
        print('Enter correct choice: S, M or L?')
        continue
    if add_pepperoni == 'Y':
        if size == 'S':
            bill += 2
        else:
            bill += 3
    if extra_cheese == 'Y':
        bill += 1
    print(f"_________________________\nYour final bill is ${bill}.\n--------------------------")

