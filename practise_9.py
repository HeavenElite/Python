## 练习 9-5
class User:
    """练习 9-5"""

    def __init__(self):
        """初始化属性"""
        self.login_attempts = 0

    def increment_login_attempts(self):
        """将属性值加1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """重置属性值"""
        self.login_attempts = 0

user  = User()
count = 0
while count <= 10:
    user.increment_login_attempts()
    count += 1
user.reset_login_attempts()
print(user.login_attempts)


## 练习 9-4
class Restaurant:
    """练习 9-4"""

    def __init__(self):
        """初始化属性"""
        self.number_served   = 0

    def set_number_served(self, customized_number):
        """设置就餐人数"""
        self.number_served = customized_number

    def increment_number_served(self, increased_number):
        """将就餐人数递增"""
        self.number_served += increased_number

restaurant = Restaurant()

restaurant.set_number_served(10)
restaurant.increment_number_served(100)
print(restaurant.number_served)

## 实例 2
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.name = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name  = f"{self.year} {self.name} {self.model} "
        long_name += f"{self.odometer_reading}"
        return long_name
    
    def read_odometer(self):
        """打印一条指出汽车历程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        重置里程表数值
        禁止将里程表读数回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

my_old_car = Car('audi', 'a4', '2019')
my_new_car = Car('audi', 'a4', '2019')

my_new_car.odometer_reading = 23
my_new_car.year = 2023
my_new_car.increment_odometer(1_000)

print(my_old_car.get_descriptive_name())
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

## 实例 1

class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.name = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = f"{self.year} {self.name} {self.model}"
        return long_name.title()
    
my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())


## 练习 3

class User:
    """练习 9-3"""

    def __init__(self, **keyargs):
        """初始化属性"""
        self.names = {}
        for first_name, last_name in keyargs.items():
            self.names[first_name.title()] = last_name.title()

    def describe_user(self):
        """描述用户"""
        print("User List:")
        count = 1
        for first_name, last_name in self.names.items():
            print(f"{count}: {first_name} {last_name}")
            count += 1
    
    def greet_user(self):
        """欢迎用户"""
        for first_name, last_name in self.names.items():
            print(f"Hello, {first_name} {last_name}!")

students_user = User(Jack='Brown', Laura='White')
students_user.greet_user()   


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