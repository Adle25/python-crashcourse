while True:
    age = int(input('Enter your age: '))

    if age < 3:
        print('Ticket is free.')
    elif age >= 3 and age < 12:
        print('Ticket will cost $10.')
    elif age >= 12:
        print('Ticket will cost $15.')