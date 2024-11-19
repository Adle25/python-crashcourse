sandwich_orders = ['pastrami', 'hot', 'diablo', 'pastrami', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'Finished sandwich {sandwich}')
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)