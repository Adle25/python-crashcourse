# Files
from pathlib import Path
import json

# path = Path('pi_million_digits.txt')
# contents = path.read_text()
# lines = contents.splitlines()

# pi_string = ''

# for line in lines:
#     pi_string += line

# birthday = input('Enter your birthday in the form mmddyy: ')

# if  birthday in pi_string:
#     print('Your birthday appears in the first million digits of pi!')
# else:
#     print('Your birthday does not appears in the first million digits of pi!')


# new_path = Path('digits.txt')

# contents = '12345467\n'
# contents += '5646456456\n'
# contents += '3242546'

# new_path.write_text(contents)

# Exceptions
# print('Give me two numbers, and I will divide them.')
# print('Enter\'q\' to quit.')

# while True:
#     first_number = input('\nFirst number: ')
#     if first_number == 'q':
#         break

#     second_number = input('Second number: ')
#     if second_number == 'q':
#         break

#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print('You cannot divide by zero!')
#     else:
#         print(answer) 

# book_path = Path('alice.txt')

# try:
#     contents = book_path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f'Sorry, the file {book_path} does not exist.')

# JSONs
numbers = [2, 3, 4, 5, 8]

json_path = Path('numbers.json')

contents = json.dumps(numbers)
json_path.write_text(contents)

file_contents = json_path.read_text()
numbers = json.loads(file_contents)
print(numbers)