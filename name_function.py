"""姓名格式调整函数"""

def get_formatted_name(first, last, middle=None):
    """生成整洁的姓名"""
    if middle:
    #   full_name = f"{first} {middle} {last}"
        pass
    else:
        full_name = f"{first} {last}"
    return full_name.title()