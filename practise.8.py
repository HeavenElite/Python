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
