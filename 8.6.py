def city_country(city, country):
    pairs = '"'+city + ","+ country +'"'
    return pairs.title()
famous_city = city_country('Paris', 'France')
print(famous_city)
