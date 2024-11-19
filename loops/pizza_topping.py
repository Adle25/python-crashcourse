prompt = '\nEnter pizza topping.'
prompt += '\nEnter \'quit\' to stop the program: '

while True:
    pizza = input(prompt)

    if pizza == 'quit':
        break

    print(pizza)