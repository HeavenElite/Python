"""调查类的模块。"""

class AnonymousSurvey:
    """收集匿名调查问卷的答案。"""

    def __init__(self, question):
        """存储一个问题，并为春初答案做准备。"""
        self.question = question
        self.response = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        self.response.append(new_response)

    def show_results(self):
        print("Survey results:")
        for response in self.response:
            print(f"- {response}")