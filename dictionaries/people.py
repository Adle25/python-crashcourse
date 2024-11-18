person_1 = {
    'first_name': 'Adilet',
    'last_name': 'Askar',
    'age': 28,
    'city': 'Almaty'
}

person_2 = {
    'first_name': 'Alisher',
    'last_name': 'Askar',
    'age': 27,
    'city': 'Qyzylorda'
}

person_3 = {
    'first_name': 'Altair',
    'last_name': 'Askar',
    'age': 19,
    'city': 'Almaty'
}

people = [person_1, person_2, person_3]

for person in people:
    print(f'{person['last_name'].title()} {person['first_name'].title()} is {person['age']} years old and lives in {person['city'].title()}')