# 练习 11-3

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """创建员工信息的测试类"""

    def setUp(self):
        """创建测试实例和所需实参"""
        self.one_employee = Employee('james', 'bond', '5000')

    def test_give_default_raise(self):
        """创建测试默认加薪的函数"""
        self.one_employee.give_raise()
        self.assertEqual(self.one_employee.salary, 10000)

    def test_give_custom_raise(self):
        """创建测试自定义加薪的方法"""
        self.one_employee.give_raise(10000)
        self.assertEqual(self.one_employee.salary, 15000)

if __name__ == '__main__':
    unittest.main()


# 练习 11.2

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试。"""

    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用。
        """ 
        question = "What language did yo first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善存储。"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.response)

    def test_store_three_response(self):
        """测试单个答案会被妥善存储。"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.response)

if __name__ == '__main__':
    unittest.main()


# 练习 11-1-2

import unittest

import city_functions


class TestCityCoutnryString(unittest.TestCase):
    """测试类: 测试城市国家字符串函数的返回值。"""

    def test_city_country(self):
        output = city_functions.formated_city_country(
            'santiago', 'chile')
        self.assertEqual(
            output, 'Santiago, Chile')

    def test_city_country_population(self):
        output = city_functions.formated_city_country(
            'santiago', 'chile', '5000000')
        self.assertEqual(
            output, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()

# 测试示例 11.1

import unittest

import name_function

class NameTestCase(unittest.TestCase):
    """测试函数模块。"""

    def test_first_last_name(self):
        """能够正确处理姓名吗？"""
        formated_name = name_function.get_formatted_name('janis', 'joplin')
        self.assertEqual(formated_name, 'Janis Joplin')
        
    def test_first_middle_last_name(self):
        """能正确处理姓名和中间名吗？"""
        formated_name = name_function.get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
    
        
if __name__ == '__main__':
    unittest.main()



# print("\nInput 'q' to quit at any time.\n")

# while True:
    # first = input("\nPlease give me a first name:\n")
    # if first == 'q':
        # break
    # last = input("\nPlease give me a last name:\n")
    # if last == 'q':
        # break

    # formated_name = name_function.get_formatted_name(first, last)
    # print(f"\nNeatly formatted name: {formated_name}")