def make_pizza(
        location, *toppings, service,
        nation='China', **customers):
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
        print(f"{first_name.title()} {last_name.title()}, ", 
                end='')
    print("\n")


def make_pizza(*args, **kwargs):
    """测试函数"""
    print(args)
    print(kwargs)


