# List basics
bicylces = ['trek', 'cannondale', 'redline', 'specialized']
print(bicylces)
print(bicylces[0].title())
print(bicylces[1].title())
print(bicylces[-1].title())

# List operations
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(1, 'BMW')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motrocycle = motorcycles.pop()
print(f'Deleted motorcycle: {popped_motrocycle}')

motorcycles.remove('BMW')
print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

sorted_cars = sorted(cars)
print(sorted_cars)
print(cars)
print(len(cars))