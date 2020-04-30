class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name.title())
        print("It is " + self.cuisine_type.title() + " cuisine.")
    def open_restaurant(self):
        print("The restaurant is open.")

restaurant = Restaurant( 'Sensei', 'Japanese')
restaurant2 = Restaurant( 'Pizza hut', 'American')
restaurant3 = Restaurant( 'Shanghai', 'Chinese') 
restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

     


