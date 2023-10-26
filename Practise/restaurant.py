"""一个可用于表示饭店的类."""

class Restaurant:
    """练习 9-6"""

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