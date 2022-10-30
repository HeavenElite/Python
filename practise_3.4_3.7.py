frute = ['Apple', 'Banana', 'Pear']
countries = ['China', 'USA', 'JP', 'Russia',frute]

print(f'The nations here were {countries[0]}, {countries[1]} and {countries[2]}.\nBut {countries.pop(2)} is falling. So, we will have {len(countries)} nations on the Earth.')

countries.append('France')
countries.insert(0,'Qing')

print(f'So, Let us welcome {countries[3]}.\nWe are sorry that the following countries are removed from this meeting: {countries.pop(1)}, {countries.pop(1)} and {countries.pop(1)}.')

countries.remove(frute)
countries.pop()

print(f'Now, the host nation of this meeting is {countries[0]}.')

del countries[0]
print(countries)