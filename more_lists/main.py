# Looping bascics
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f'Magician {magician.title()}, that was a great trick!')
    print(f'I can not wait to see your next trick, {magician.title()}.\n')

print('Thank you, everyone. That was a great magic show!')

# Ranges
for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []

for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(sum(digits))
print(min(digits))
print(max(digits))

triplets = [value ** 3 for value in range(1, 11)]
print(triplets)

# List slices
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[::-1])

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print(f'My favorite foods are: {my_foods}')
# print(f'Fried favorite foods are: {friend_foods}')

# Tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for value in dimensions:
    print(value)