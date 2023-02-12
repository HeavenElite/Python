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

