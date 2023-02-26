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