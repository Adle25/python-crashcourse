def describe_city(city_name, country_name='kazakhstan'):
    print(f'{city_name.title()} is a capital of {country_name.title()}')

describe_city('Astana')
describe_city('London', 'UK')
describe_city(country_name='Brazil', city_name='Rio')
describe_city('Riyadh', country_name='UAE')