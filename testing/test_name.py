from name import get_formatted_name


def test_first_last_name():
    formatted_name = get_formatted_name('adilet', 'askar')
    print(formatted_name)
    assert formatted_name == 'Adilet Askar'

def test_first_last_middle_name():
    formatted_name = get_formatted_name('adilet', 'askar', 'erlanuly')
    assert formatted_name == 'Adilet Erlanuly Askar'