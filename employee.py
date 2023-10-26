"""雇员类的模块。"""

class Employee():
    """定义雇员类。"""

    def __init__(self, name, surname, salary):
        """初始化雇员信息属性。"""
        self.name = name.title()
        self.surname = surname.title()
        self.salary = int(salary)

    def give_raise(self, number='5000'):
        self.salary += int(number)