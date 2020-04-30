class Users():
    def __init__(self, first_name, last_name, location, age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
    def describe_user(self):
        print("The name of the user is " + self.first_name.title()+" " + self.last_name.title() + ".")
        print("The age of the user is " + str(self.age) + ".")
        print("The location of the user is " + self.location + ".")
    def greet_user(self):
        print("What's up " + self.first_name.title() + ' '+ self.last_name.title())

user = Users('Aiden', 'Pompa', 'US', 18)
user.describe_user()
user.greet_user()

user2 = Users('Ian', 'Lehman', 'Italy', 29)
user2.describe_user()
user2.greet_user()
