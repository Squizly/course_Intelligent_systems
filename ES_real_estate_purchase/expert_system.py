import re

class RealEstateExpert:

    def __init__(self, questions, rules):

        # === === === === === === === === === === === === === === === === === #
        # Инициализация экспертной системы :
        # questions - список вопросов, которые будем задавать пользователю
        # rules - правила, по которым система будет выдавать результат
        # === === === === === === === === === === === === === === === === === #

        self.questions = questions
        self.rules = rules

    def get_facts(self):

        # === === === === === === === === === === === === === === === === === #
        # Принимает данные от пользователя для подбора недвижимости
        # === === === === === === === === === === === === === === === === === #

        self.facts = dict()

        for question in self.questions:
            
            while True:
                answer = input(question["Вопрос"])

                if self.validate_input(question["Ключ"], answer):
                    self.facts[question["Ключ"]] = answer
                    break
                    
                else:
                    print("Некорректный ввод. Пожалуйста, попробуй снова.")
    
    def validate_input(self, question, answer):

        # === === === === === === === === === === === === === === === === === #
        # Проверяем корректность ввода ответов пользователем
        # === === === === === === === === === === === === === === === === === #

        if question == "Бюджет":
            
            if re.fullmatch(r'\d+', answer):
                return int(answer) > 0
        
        elif question == "Семейное положение":
            return answer in ["Да", "Нет"]
        
        elif question == "Количество детей":

            if re.fullmatch(r'\d+', answer):
                return 0 <= int(answer) <= 5
        
        elif question == "Инфраструктура":
            return answer in ["Очень важно", "Не критично"]

        return False

    
    def fit(self):

        # === === === === === === === === === === === === === === === === === #
        # Получаем ответы на вопросы, проверяем их корректность и накладываем ограничения
        # Получаем рекомендации прямой проверкой условий
        # === === === === === === === === === === === === === === === === === #

        # Получим ответы от пользователя на заданные вопросы :
        self.get_facts()

        # Рассмотрим частный случай , когда бюджет менее 1 млн. рублей --->
        if (int(self.facts["Бюджет"]) <= 1_000_000):
            print("К сожалению, такого бюджета недостаточно для покупки недвижимости.")
            print("Или же вы можете рассмотреть коммунальное жилье.")
            return
        
        # Преобразуем бюджет из числового типа в категориальный --->
        self.convert_budget_to_category_type()

        # Посомтрим что у нас получилось по ответам
        print("Ваши ответы:", self.facts)

        # Пройдемся по правилам , составляя список рекомендаций, топ-3 варианта для покупки --->
        # Список для результата работы экспертной системы
        self.recommendations = []

        for current_estate in self.rules:
            
            score = 0

            for key,value in current_estate["Условия"].items():

                if key in self.facts and (self.facts[key] == value or callable(value)):
                    
                    # Проверяка на лямбда-функцию ---> Количество детей
                    if (callable(value)):
                        value(int(self.facts[key]))

                    score += 25

            self.recommendations.append((current_estate["Результат"], score))

        
        # Посмотрим что насобирали
        self.recommendations.sort(key = lambda x : x[1], reverse=True)

        print("\nРекомендованные варианты (от наилучшего к менее подходящему):")
        self.recommendations = [rec for rec in self.recommendations if rec[1] > 0][:3]

        if self.recommendations:
            for target, score in self.recommendations:
                print(f"Вариант: {target} | Балл: {score:.2f}")
        else:
            print("Нет подходящих вариантов. Попробуйте изменить условия.")

    def backward_chaining(self, goal, facts, visited=None):
        # === === === === === === === === === === === === === === === === === #
        # Обратный цепочечный вывод
        # goal - конечная цель
        # facts - известные факты
        # === === === === === === === === === === === === === === === === === #

        if visited is None:
            visited = set()

        if goal in facts:
            return True
        
        if goal in visited:
            return False
        
        visited.add(goal)

        for rule in self.rules:
            if rule["Результат"] == goal:
                print("rule == goal")
                condition_met = True

                for condition in rule["Условия"].values():
                    # TO DO::: ПРОВЕРКА ЛЯМБДА ФУНКЦИЙ НЕ ПРОХОДИТ!
                    if self.backward_chaining(condition, facts, visited) is False:
                        print(f"condition = {condition} ---> не выполнилось.")
                        condition_met = False
                        break

                if condition_met:
                    print("all condition is met")
                    facts.add(goal)
                    return True
                
        return False



    def convert_budget_to_category_type(self):

        # === === === === === === === === === === === === === === === === === #
        # Преобразуем бюджет из числового типа в категориальный
        # === === === === === === === === === === === === === === === === === #

        budget = int(self.facts["Бюджет"])

        if budget <= 2_000_000:
            self.facts["Бюджет"] = "До 2 млн. рублей"

        elif budget <= 3_000_000:
            self.facts["Бюджет"] = "До 3 млн. рублей"
        
        elif budget <= 6_000_000:
            self.facts["Бюджет"] = "От 3 до 6 млн. рублей"
        
        else:
            self.facts["Бюджет"] = "Более 6 млн. рублей"

        return 