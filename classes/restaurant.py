class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'This is {self.cuisine_type} restaurant named {self.restaurant_name.title()}.')

    def open_restaurant(self):
        print(f'{self.restaurant_name.title()} is now open!')

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanil', 'chocolate', 'banana']

    def get_flovers(self):
        for flavor in self.flavors:
            print(flavor)


first_restaurant = Restaurant('salsabil', 'eastern')
first_restaurant.describe_restaurant()
first_restaurant.open_restaurant()

second_restaurant = Restaurant('koreana', 'korean')
second_restaurant.describe_restaurant()

third_restaurant = Restaurant('mama mia', 'italian')
third_restaurant.describe_restaurant()

test_restaurant = Restaurant('adle', 'kazakh')
print(test_restaurant.number_served)

test_restaurant.number_served = 10
print(test_restaurant.number_served)

test_restaurant.set_number_served(30)
print(test_restaurant.number_served)

test_restaurant.increment_number_served(20)
print(test_restaurant.number_served)

ice_cream_stand = IceCreamStand('cremo', 'ice cream')
ice_cream_stand.get_flovers()