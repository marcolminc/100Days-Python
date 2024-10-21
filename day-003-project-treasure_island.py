print('Welcome to Treasure Island\nYour mission is to find the treasure')
choice = input('You are at a crossroad, which direction do you choose: left or right?\n').lower()
if choice == 'left':
    choice = input('You arrived at a lake. type wait to wait for a boat or swim: ').lower()
    if choice == 'wait':
        print('you have arrived at a shore unharmed')
        choice = input('Choose a dor (Red, Yellow or Blue)?\n').lower()
        if choice == 'red':
            print('Entered a furnace!\nGame over.')
        elif choice == 'blue':
            print('Entered room of angry beasts!\nGame over.')
        elif choice == 'yellow':
            print('Treasure!\nYou win!')
        else:
            print('Game over.')
    else:
        print('You are attacked by trout...\nGame over.')
else:
    print('You have fallen into a hole!\nGame over.')