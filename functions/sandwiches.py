def get_sandwich(*items):
    print('\nYou orderd a sandwich with the following items:')

    for item in items:
        print(f'---{item}')


get_sandwich('bacon')
get_sandwich('tuna', 'salad')