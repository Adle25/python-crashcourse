def get_city_country(city, country, population=''):
    if not population:
        result = f'{city.title()}, {country.title()}'
    else:
        result = f'{city.title()}, {country.title()}, population -- {population}'

    return result