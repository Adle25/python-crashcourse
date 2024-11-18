rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'muatu': 'nigeria'
}

for name, country in rivers.items():
    print(f'{name.title()} runs through {country.title()}')