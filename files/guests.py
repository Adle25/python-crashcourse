from pathlib import Path

names = ''

while True:
    name = input('(Enter \'q\' to quit)\nHello, please enter your name: ')
    if name == 'q':
        break

    names += f'{name}\n'

path = Path('guests.txt')
path.write_text(names)
