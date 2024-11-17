current_users = ['admin', 'sarah', 'conor', 'blake', 'mercury']
new_users = ['admin', 'roy', 'pirro', 'sam', 'altman']

for user in new_users:
    if user.lower() in current_users:
        print(f'{user.title()} need to create new username.')
    else:
        print(f'{user.title()} username is available')
