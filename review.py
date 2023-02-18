## 复习 7

alien = {

}
key = 'color'
value = 'green'

alien[key] = value

print(alien.get('name',))

## 复习 6

import Function as f

f.make_pizza(
    'Beijing', 'Apple', 'Banada', '123',
    nation='USA', lauris='nie', james='zhang', service='VIP'
    )

## 复习 5

def make_pizza(location, *toppings, service, nation='China', **customers):
    """打印顾客点的所有配料"""
    print()
    print(f"User service level is: {service.title()}.")
    print(f"User location is: {location.title()}.")
    print(f"User nation is: {nation.title()}.")
    print(f"User topppings are:", end=' ')
    for topping in toppings:
        print(topping.title(), end=', ')
    print("\nUser name is ", end='')
    for first_name, last_name in customers.items():
        print(f"{first_name.title()} {last_name.title()}, ", end='')
    print("\n")

make_pizza('Beijing', 'Apple', 'Banada', nation='USA', service='VIP', lauris='nie', james='zhang')

## 复习 4

def make_pizza(location, toppings='Meet', service='normal'):
    """打印顾客点的所有配料"""
    print()
    print(f"User service Level is: {service.title()}.")
    print(f"User location is: {location.title()}.")
    print(f"User topppings are: ", end='')
    for topping in toppings:
        print(topping.title(), end=', ')
    print("\n")

make_pizza('Beijing', service='VIP')


## 复习 3

def make_pizza(location, *toppings, service='normal'):
    """打印顾客点的所有配料"""
    print()
    print(f"User service Level is: {service.title()}.")
    print(f"User location is: {location.title()}.")
    print(f"User topppings are:", end=' ')
    for topping in toppings:
        print(topping.title(), end=', ')
    print("\n")

make_pizza('Beijing', 'Apple', 'Banada', service='VIP')

## 复习 2

def greet_users(names=['lauris']):
    """向列表中每位用户发出简单问候"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


## 复习 1

def formatted_name(givenname='qi', sirname='nie', middlename=None):
    """返回整洁的姓名"""
    if middlename:
        full_name = {
            'Given Name': givenname.title(),
            'Sir Name': sirname.title(),
            'Middle Name': middlename.title(),
            }
    else:
        full_name = f"{givenname} {sirname}".title()
    return full_name

while True:
    prompt_first   = "\nPlease input your first name:\n\n"
    user_first     = input(prompt_first)
    
    prompt_last    = "\nPlease input your last name:\n\n"
    user_last      = input(prompt_last)

    prompt_middle  = "\nPlease input your middle name:\n\n"
    user_middle    = input(prompt_middle)

    full_name = formatted_name(user_first, user_last, user_middle)
    print(f"\nYour full name is {full_name}.\n")

