"""城市和国家的字符串格式校正函数"""

def formated_city_country(city, country, population=None):
    if population:
        string = f"{city.title()}, {country.title()} - population {population}"
    else:
        string = f"{city.title()}, {country.title()}"
    return string

