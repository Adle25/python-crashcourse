from city_country import get_city_country


def test_city_country():
    result = get_city_country('astana', 'kazakhstan')
    assert result == 'Astana, Kazakhstan'

def test_population():
    result = get_city_country('astana', 'kazakhstan', 1_000_000)
    assert result == 'Astana, Kazakhstan, population -- 1000000'