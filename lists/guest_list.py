guests = ['Azhe', 'Arys', 'Papa']

message = f'Glad to see you, {guests[0]}'
print(message)

message = f'Glad to see you, {guests[1]}'
print(message)

message = f'Glad to see you, {guests[2]}'
print(message)

print(f'{guests[0]} can not come today')
guests[0] = 'Mama'

message = f'Glad to see you, {guests[0]}'
print(message)

message = f'Glad to see you, {guests[1]}'
print(message)

message = f'Glad to see you, {guests[2]}'
print(message)

print('I found a bigger table so more guests are welcome!')

guests.insert(0, 'Mans')
guests.insert(2, 'Alisher')
guests.append('Chinga')

message = f'Glad to see you, {guests[0]}'
print(message)

message = f'Glad to see you, {guests[1]}'
print(message)

message = f'Glad to see you, {guests[2]}'
print(message)

message = f'Glad to see you, {guests[3]}'
print(message)

message = f'Glad to see you, {guests[4]}'
print(message)

message = f'Glad to see you, {guests[5]}'
print(message)

print('Sorry I can invite only 2 guests!')

person = guests.pop()
message = f'Sorry, {person} I cannot invite you'
print(message)

person = guests.pop()
message = f'Sorry, {person} I cannot invite you'
print(message)

person = guests.pop()
message = f'Sorry, {person} I cannot invite you'
print(message)

person = guests.pop()
message = f'Sorry, {person} I cannot invite you'
print(message)

message = f'Glad to see you, {guests[0]}'
print(message)

message = f'Glad to see you, {guests[1]}'
print(message)

print(guests)

del guests[0]
del guests[0]

print(guests)
