import pytest
from employee import Employee


@pytest.fixture
def get_employee():
    test_employee = Employee('Adilet', 'Askar', 20000)
    return test_employee

def test_give_default_raise(get_employee):
    get_employee.give_raise()

    assert 25000 == get_employee.annual_salary

def test_give_custom_raise(get_employee):
    get_employee.give_raise(10000)

    assert 30000 == get_employee.annual_salary