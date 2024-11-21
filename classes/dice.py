from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        side_number = randint(1, self.sides)
        print(f'Rolling .... {side_number}')


my_die = Die()
my_die.roll_die() 