# Function basics
def greet_user(username):
    print(f'Hello, {username.title()}!')


greet_user('Adilet')

# Passing arguments
def describe_pet(pet_name, animal_type='dog'):
    print(f'\nI have {animal_type}.')
    print(f'My {animal_type}\'s name is {pet_name.title()}.')


describe_pet('hamster', 'harry')
describe_pet(animal_type='dog', pet_name='willie')
describe_pet('black')

# Return values
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f'{first_name} {last_name} {middle_name}'
    else:
        full_name = f'{first_name} {last_name}'

    return full_name.title()

musician = get_formatted_name('adilet', 'askar', 'erlanuly')
print(musician)

def build_person(first_name, last_name, age=None):
    person = {
        'first': first_name,
        'last': last_name
    }

    if age:
        person['age'] = age

    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# List passing
def greet_users(names):
    for name in names:
        msg = f'Hello, {name.title()}!'
        print(msg)


usernames = ['hannah', 'jim', 'sarah']
greet_users(usernames)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print(f'\nThe following models have benn prined:')
    for model in completed_models:
        print(model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

def make_pizza(size, *toppings):
    print(f'\nMaking {size}-inch the pizza with the following toppings:')

    for topping in toppings:
        print(f'- {topping}')

make_pizza(2, 'mushrooms', 'peperroni', 'olives')

def build_profile(first, last, **user_info ):
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', filed='physics')
print(user_profile)

# import cars

# car = cars.make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)

from cars import make_car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
