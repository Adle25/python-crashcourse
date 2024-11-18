pet_1 = {
    'kind': 'dog',
    'owner': 'sarah'
}

pet_2 = {
    'kind': 'cat',
    'owner': 'mikah'
}

pet_3 = {
    'kind': 'pig',
    'owner': 'lorene'
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f'{pet['owner'].title()} has got {pet['kind']}')
