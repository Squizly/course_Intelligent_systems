from knowledge_base.questions import questions

class RealEstateExpertSystem():

    def __init__(self, questions):
        self.questions = questions
    
    def get_facts(self):
        # Получаем ответы на вопросы от пользователя в словарь facts
        self.facts = dict()

        for ask in self.questions:
            self.facts[ask["Ключ"]] = input(ask["Вопрос"])
    
    def print_answers_user(self):
        # Вывод ответов пользователя
        for key,value in self.facts.items():
            print(f"{key} : {value}")
    
    def predict(self):
        # Учитывая ответы пользователя , строим цепочку выводов

        if self.check_correct_budget() is False:
            print("Рекомендую увеличить бюджет.")
            return
        
        # Сделаем скоринг для каждого варианта, чтоб вывести топ вариантов

        #...

    def check_correct_budget(self):
        # TO DO:: переделать
        if (int(self.facts["Бюджет"]) < 1_000_000):

            if (self.facts["Ипотека"] == "Нет"):
                print("Ваш бюджет слишком мал для покупки недвижимости.")
                return False
            
            self.facts["Бюджет"] = "Низкий"

        elif (int(self.facts["Бюджет"]) < 3_000_000):
            self.facts["Бюджет"] = "Низкий"

        elif (int(self.facts["Бюджет"]) < 5_000_000):
            self.facts["Бюджет"] = "Средний"

        else:
            self.facts["Бюджет"] = "Высокий"
        
        return True



if __name__ == "__main__":

    system = RealEstateExpertSystem(questions)
    system.get_facts()
    system.print_answers_user()
    system.predict()