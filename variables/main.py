# Variables
message = 'Hello Python World!'
print(message)

message = 'Hello Python Crashcourse World!'
print(message)

# Strings
simple_str = 'this is a simple string'
print(simple_str.title())
print(simple_str.upper())
print(simple_str.lower())

first_name = 'adilet'
second_name = 'askar'
full_name = f'Hello, {first_name.title()} {second_name.title()}'
print(full_name)

print('\tPython')
print('Languages:\n\tPython\n\tC++\n\tGo')

favorite_language = 'python  '
print(len(favorite_language))
print(len(favorite_language.rstrip()))

nostarch_url = 'https://nostarch.com'
pref = 'https://'
print(nostarch_url.removeprefix(pref))

# Numbers
print(2 + 2)
print(3 - 1)
print(3 * 2)
print(3 / 2)
print(2 ** 2)
print(0.1 + 0.1)
print(0.2 * 2)
print(0.3 / 3)
print(1 + 2.0)

universe_age = 14_000_000_000
print(universe_age)

first_number, second_number = 1, 2
first_number, second_number = 2, 1
print(first_number, second_number)