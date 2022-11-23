age = 33
art = 'a'

if (age < 2):
    title = 'Baby'
elif (age >= 2) and (age < 4):
    title = 'Kid'
elif (age >= 4) and (age < 13):
    title = 'Child'
elif (age >= 13) and (age < 20):
    title = 'Teenage'
elif (age >= 20) and (age < 65):
    title = 'Adult'
    art = 'an'
else:
    title = 'Old Person'
    art = 'an'

print("This person is {} {}.".format(art, title))

favorite_fruits = ['apple', 'banana', 'pear']
favorite_fruit  = 'melon'

if favorite_fruit in favorite_fruits:
    print(f"{favorite_fruit} is in the list.")

if favorite_fruit not in favorite_fruits:
    print(f"{favorite_fruit.title()} is NOT in the list.")