class Users():
    def __init__(self, first_name, last_name, location, age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.login_attempts = 0
    def describe_user(self):
        print("The name of the user is " + self.first_name.title()+" " + self.last_name.title() + ".")
        print("The age of the user is " + str(self.age) + ".")
        print("The location of the user is " + self.location + ".")
    def greet_user(self):
        print("What's up " + self.first_name.title() + ' '+ self.last_name.title())
    def read_login(self):
        print("You have tried logging in " + str(self.login_attempts) + " times.")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

user = Users('Aiden', 'Pompa', 'US', 18)
user.increment_login_attempts()
user.increment_login_attempts()
user.read_login()
user.reset_login_attempts()
user.read_login()
