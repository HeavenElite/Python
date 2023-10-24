"""练习使用的函数汇总"""

def input_collection():
    """搜集用户提供的浮点数并返回"""
    while True:
        try:
            number = input("Please provide a number:\n")
            number = float(number)
        except:
            print("Please provde a number instead of words.\n")
            continue
        else:
            break
    return number
        


def quit_confirmation():
    """询问用户是否退出程序"""
    prompt  = "Do you want to continue this program?\n"
    prompt += "If you don't, please input q or Q\n"
    confirm = input(prompt)
    check_confirm = confirm.lower()

    if check_confirm != 'q':
        confirm = 'continue'
    elif check_confirm == 'q':
        confirm = 'quit'
    return confirm

def count_words(filename):
    """计算一个文件包含多少个单词"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exsits.")
    else:
        words = contents.split()
        num_words = len(words)
    return num_words


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


def build_dictionary():
    """"Build a dictionary by user inputings."""
    flag = 'start'
    dictionary = {}
    while flag != 'stop':
        key = input("Please provide the Key:\n")
        value = input("Please provide the value:\n")
        dictionary[key] = value
        flag = input("Continue to add? Input 'Stop' to quit.\n")
        flag = flag.lower()
    return dictionary
