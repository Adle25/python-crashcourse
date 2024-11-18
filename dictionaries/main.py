# Dictinary basics
first_alien = {
    'color': 'green',
    'points': 5
}

print(first_alien['color'])
print(first_alien['points'])
print(first_alien)

first_alien['x_position'] = 0
first_alien['y_position'] = 25
print(first_alien)

first_alien['color'] = 'yellow'
print(first_alien)

del first_alien['points']
print(first_alien)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

language = favorite_languages['sarah'].title()
print(f'Sarah\'s favorite language is {language}')

print(favorite_languages.get('new'))

user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
}

for key, value in user_0.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')

for key in user_0.keys():
    print(key)

for value in user_0.values():
    print(value)

# Sets
languages = {'python', 'rust', 'python', 'c'}
print(languages)

# Nesting
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)