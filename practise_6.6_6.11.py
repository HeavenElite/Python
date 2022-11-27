person = {
    'city': 's',
    'given_name': 33,
    'surname': 'nie',

}


print(person.values())
print(set(person.values()))


#properties = ['given_name', 'surname', 'age', 'city', 'country']

#for property in properties:
#    if person.get(property) != None:
#        print(f"The Key {property.title()} is existing.")
#    elif person.get(property) == None:
#        print(f"Please set a new value for this Key: {property.title()}")


cities = {
    'hongkong': {
        'nation': 'china',
        'population': 100_000_000,
        'fact': "It's not as good as before"
        },
    'new york': {
        'nation': 'usa',
        'population': 200_000_000, 
        'fact': "Still the center of Intl. finance",
        },
    'tokyo': {
        'nation': 'japan',
        'population': 400_000_000,
        'fact': "Maybe not so OK",
        },
    }

for city, infor in cities.items():
    print(f"\n{city.title()}")
    for key in infor:
        value = infor.get(key)
        if key == 'population':
            print(f"\tThe {key.title()} is {value}.")
        elif key == 'nation':
            print(f"\tThe {key} is {value.title()}.")
        elif key == 'fact':
            print(f"\tThe {key} is {value}.")