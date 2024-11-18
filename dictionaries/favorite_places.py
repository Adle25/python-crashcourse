favorite_places = {
    'adilet': ['japan', 'saudi arabia', 'south korea'],
    'almira': ['usa', 'uk'],
    'farida': ['uae', 'turkey']
}

for name, places in favorite_places.items():
    print(name, end='\t')
    for place in places:
        print(place, end='\t')

    print()