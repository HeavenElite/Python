from user import *

class Priviledges:
    """权限汇总."""

    def __init__(self):
        self.priviledges = [
            "can add post",
            "can delete post",
            "can ban user",
            ]

    def show_priviledge(self):
        """显示管理员权限"""
        print(f"The Administrator permissions are:")
        for priviledge in self.priviledges:
            print(f"{priviledge.title()}")

class Admin(User):
    """管理页的独特之处."""

    def __init__(self, **keyargs):
        """
        先初始化父类属性.
        再初始化管理页属性.
        """
        super().__init__(**keyargs)
        self.priviledge = Priviledges()