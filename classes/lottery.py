from random import choice

lottery = [2, 1, 32, 43, 35, 535, 353, 3, 0, 12, 'A', 'D', 'C', 'B']

first_choice = choice(lottery)
second_choice = choice(lottery)
third_choice = choice(lottery)
fourth_choice = choice(lottery)

print(f'Any ticket matching {first_choice} {second_choice} {third_choice} {fourth_choice} is winning!')