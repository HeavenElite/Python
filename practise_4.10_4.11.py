numbers = [value for value in range(1,11)]
print(numbers)


my_pizza = ['meet', 'frute', 'vegetable']
friend_pizza = my_pizza[:]

my_pizza.insert(0,'banana')
friend_pizza.append('appple')

print('My favorite pizzas are:')
for pizza in my_pizza:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)