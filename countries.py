import json 
from pygal.maps.world import COUNTRIES
filename = 'population_data.json'
with open(filename) as f:
    country_data = json.load(f)

for con_dict in country_data:
    if con_dict['Year'] == '2010':
        country_name = con_dict['Country Name']
while country_name:
    def get_country_code(country_name):

        for code, name in COUNTRIES.items():
            if name == country_name:
                print(code)
            else:
                return None
    
    
