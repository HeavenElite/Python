## 练习 2

class Restaurant:
    """练习 9-1"""

    def __init__(self, name, *args):
        """初始化属性"""
        self.restaurant_name = name
        self.cuisine_type    = ''
        count = 0
        for type in args:
            count += 1
            if count < len(args):
                self.cuisine_type += f"{type.title()}, "
            if count == len(args):
                self.cuisine_type += f"{type.title()}."

    def describe_restaurat(self):
        """餐馆描述"""
        output_describe  = f"{self.restaurant_name.title()} serves with "
        output_describe += f"cuisine types:\n"
        output_describe += f"{self.cuisine_type}"
        print(output_describe)

    def open_restaurant(self):
        """餐馆状态"""
        output_openstatus  = f"The Restaurant, {self.restaurant_name} is "
        output_openstatus += f"Opening now."
        print(output_openstatus)


beijing_restaurant = Restaurant(
    '山西美食', 
    '刀削面', '肉夹馍', '凉皮'
    )

print(beijing_restaurant.restaurant_name)
print(beijing_restaurant.cuisine_type)

beijing_restaurant.describe_restaurat()
beijing_restaurant.open_restaurant()


sichuan_restaurant = Restaurant(
    '川菜馆', 
    '鱼香肉丝', '米饭'
    )

print(sichuan_restaurant.restaurant_name)
print(sichuan_restaurant.cuisine_type)

sichuan_restaurant.describe_restaurat()
sichuan_restaurant.open_restaurant()


dongbei_restaurant = Restaurant(
    '东北烤冷面', 
    '烤冷面'
    )

print(dongbei_restaurant.restaurant_name)
print(dongbei_restaurant.cuisine_type)

dongbei_restaurant.describe_restaurat()
dongbei_restaurant.open_restaurant()

## 练习 1

class Dog:
    """一次模拟小狗的简单尝试。"""
    
    def sit(self):
        """模拟小狗收到命令时蹲下。"""
        print(f"{self.good} is now sitting.")

    def __init__(self, name, age):
        """初始化属性 name 和 age。"""
        self.good = name
        self.age  = age + 1


first_dog = Dog('Brown', 8)

print(first_dog.good)