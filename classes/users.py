class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f'\nUser firstname: {self.first_name}')
        print(f'User lastname: {self.last_name}')
        print(f'User age: {self.age}')

    def greet_user(self):
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()


adilet = User('adilet', 'askar', 28)
print(adilet.first_name)
print(adilet.last_name)
print(adilet.age)
print('----------------')
adilet.describe_user()
adilet.greet_user()

adilet.increment_login_attempts()
adilet.increment_login_attempts()
adilet.increment_login_attempts()
adilet.increment_login_attempts()
print(adilet.login_attempts)

adilet.reset_login_attempts()
print(adilet.login_attempts)

admin = Admin('altair', 'askar', 19)
admin.privileges.show_privileges()


    