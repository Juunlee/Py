import json

filename = 'favnumber.json'
number = input("What is your favorite number?")
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)
with open(filename) as f_obj:
    json.load(f_obj)
    print("I know your favorite number! It is " + number + ".")
    



