# Conditionals
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if  car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushroom'

if requested_topping != 'anchovies':
    print('Hold th anchoives')

age_first = 22
age_second = 17

print(age_first > 18 and age_second > 18)
print(age_first > 18 or age_second > 18)

requested_toppings = ['mushroom', 'onions', 'pineapple']

print('mushroom' in requested_toppings)
print('anchoives' not in requested_toppings)

# If statements
age = 16

if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote?')
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

age = 12

if age < 4:
    print('Your admission cost is $0.')
elif age < 18:
    print('Your admission cost is $25.')
else:
    print('Your admission cost is $40.')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
