# Class basics
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name.title()} is now sitting.')

    def roll_over(self):
        print(f'{self.name.title()} rolled over.')


my_dog = Dog('willie', 6)

print(f'My dog\'s name is {my_dog.name.title()}.')
print(f'My dog is {my_dog.age} years old.')

my_dog.sit()
my_dog.roll_over()

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has {self.battery_size}-kWh battery.')

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f'This car can go about {range} miles on a full charge.')

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
    


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cannot rollback the odometer reading.')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_car = Car('audi', 'a4', 2024)
print(my_car.get_descriptive_name())
my_car.read_odometer()

my_car.odometer_reading = 23
my_car.read_odometer()

my_car.update_odometer(35)
my_car.read_odometer()

my_car.increment_odometer(2)
my_car.read_odometer()

electric_car = ElectricCar('nissan', 'leaf', 2024)
print(electric_car.get_descriptive_name())
electric_car.battery.describe_battery()
electric_car.battery.get_range()
electric_car.battery.upgrade_battery()
electric_car.battery.get_range()

from random import randint, choice

print(randint(1, 8))

players = ['Vinicius Jr.', 'Rodrygo', 'Mbappe', 'Bellingham', 'Cavaminga']
print(choice(players))