class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name.title())
        print("It is " + self.cuisine_type.title() + " cuisine.")
    def open_restaurant(self):
        print("The restaurant is open.")
    def number_customers(self):
        print(str(self.number_served) + " people are served in this restaurant")
    def set_number_served(self, people):
        self.number_served = people
        print(str(self.number_served) + " people are newly served in this restaurant.")
    def increment_number_served(self, increment):
        self.number_served += increment
        
              
restaurant = Restaurant( 'Sensei', 'Japanese')
restaurant.number_customers()
restaurant.set_number_served(102)
restaurant.increment_number_served(200)
restaurant.number_customers()
     
