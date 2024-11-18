cities = {
    'London': {
        'country': 'UK',
        'population': 1000
    },
    'Rio': {
        'country': 'Brazil',
        'population': 3000
    },
    'Almaty': {
        'country': 'Kazakhstan',
        'population': 100
    }
}

for city, factors in cities.items():
    print(f'{city.title()}:')
    for k, v in factors.items():
        print(f'\t{k}: {v}')