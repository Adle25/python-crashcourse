while True:
    print('\n(Enter \'q\' to exit)')
    first_number = input('Enter first number: ')

    if first_number == 'q':
        break
    
    second_number = input('Enter second number: ')

    if second_number == 'q':
        break

    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print('Please provide numbers!')
    else:
        print(f'The result is: {result}')