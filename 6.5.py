Rivers_0 = {'Nile' : 'Egypt', 'Tigris' : 'Iraq', 'Tiber' : 'Italy'}
for river, country in Rivers_0.items():
    print(river.title()+" " +"runs through"+" "+ country.title()) 
for river in Rivers_0.keys():
    print(river.title())
for country in Rivers_0.values():
    print(country.title())
