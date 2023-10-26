"""一组可以表示 Admin 的类"""

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