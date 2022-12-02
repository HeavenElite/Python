def display_message(knowledge):
    """显示本章所学的知识"""
    print(f"What I learnd in this chapter is \"{knowledge.title()}\".")

display_message('while language')

## Practise 8-4
#- 

def make_shirt(size, type='I love Python'):
    """显示T恤的尺码和字样"""
    print(f"The size is {size.upper()}.")
    print(f"The type is {type.title()}.")

make_shirt('l')
print()
make_shirt('XL', 'China')


## Practise 8-5
#- 注意为函数添加文档字符串

def describe_city(name, nation):
    """显示城市的名字和所述的国家"""
    print(f"{name.title()} is in {nation.title()}")

resorts = {
    'beijing': 'china',
    'new york': 'usa',
    'Tokyo': 'japan',
    }

print()

for name, nation in resorts.items():
    describe_city(nation=nation, name=name)

print()

## Practise 8-6

def city_country(city, nation):
    """返回城市字符串"""
    formated_string = f"{city.title()}, {nation.title()}"
    return formated_string

city_data = {
    'beijing': 'china',
    'shanghai': 'china',
    'new york': 'united states',
    }

for city, country in city_data.items():
    feedback = city_country(city, country)
    print(feedback)

## Practise 8-8
#- lower()不要写成lower，方法也要加圆括号
#- while成功终止后，要有print()说明循环已成功终止，或者感谢用户的配合。

def make_album(singer, album, number = 0):
    """生成音乐集"""
    if number:
        music = {
            'singer': singer.title(),
            'album': album.title(),
            'number': number,
            }
    else:
        music = {
            'singer': singer.title(),
            'album': album.title(),
            }

    return music

active = True

while active:
    singer = input("\nPlease tell me your favorite singer's name:\n")
    if singer.lower() == 'quit':
        break
    album  = input("\nWhat is your favorite album?\n")
    if album.lower() == 'quit':
        break

    formated_data = make_album(singer, album)
    print(f"\n{formated_data}\n")

print("\nThanks for responsding!\n")

## Practise 8-10
#- 复习第七章，修改列表数据，使用while循环

def delivery_message(information):
    """输出消息"""
    while information:
        infor = information.pop(0)
        print(f"\n{infor}\n")
        send_messages.append(infor)

send_messages = []
information = [
    "It's a good day.",
    "Are you OK?",
    "Good morning~"
    ]

delivery_message(information)

print(information)
print(send_messages)

## Practise 8-12

def collect_material(*args):
    """收集单值实参"""
    print(f"\nBelow is the material you ordered:")
    for material in args:
        print(f"\t- material")


collect_material('apple')

## Practise 8-13

def build_profile(firstname, lastname, **user_info):
    """生成字典"""
    user_info['firstname'] = firstname
    user_info['lastname'] = lastname
    
    return user_info

user_info = build_profile('james', 'brone', location = 'beijing', website = 'www.baidu.com')
print(user_info)

## Practise 8-14

def make_car(brand, model, **kwargs):
    kwargs['brand'] = brand
    kwargs['model'] = model

    return kwargs

car_info = make_car('subara', 'outback', color='blue', tow_package=True)
print(car_info)

