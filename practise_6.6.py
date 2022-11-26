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