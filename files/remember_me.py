from pathlib import Path
import json

def get_stored_data(path):
    if path.exists():
        contents = path.read_text()
        data = json.loads(contents)
        return data
    else:
       return None
    
def get_new_username(path):
    username = input("What is your name: ")
    age = int(input('What is your age: '))
    city = input('What city you live: ')
    result_dict = {}
    result_dict['username'] = username
    result_dict['age'] = age
    result_dict['city'] = city
    contents = json.dumps(result_dict)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('username.json')
    data = get_stored_data(path)
    if data:
        correct_username = input(f'Is {data['username']} is correct (yes/no): ')
        if correct_username == 'yes':
            print(f"Welcome back, {data['username']}, {data['age']} years old, leaving in {data['city'].title()}!")
        elif correct_username == 'no':
            username = get_new_username(path)
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
