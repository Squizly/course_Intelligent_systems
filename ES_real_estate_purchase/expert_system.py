class RealEstateExpertSystem:

    def __init__(self, questions, rules):
        # Инициализация экспертной системы
        self.questions = questions
        self.rules = rules
        self.facts = {}

    def get_facts(self):
        # Получаем ответы на вопросы от пользователя
        for question in self.questions:
            while True:
                answer = input(question["Вопрос"])
                if self.validate_input(question, answer):
                    self.facts[question['Ключ']] = answer
                    break
                else:
                    print("Некорректный ввод. Пожалуйста, попробуйте снова.")

    def validate_input(self, question, answer):
        # Валидация ответа пользователя для конкретного вопроса
        key = question["Ключ"]

        if key == "Бюджет":
            try:
                value = int(answer)
                return value > 0
            except ValueError:
                return False

        elif key in ("Ипотека", "Семейное положение"):
            return answer in ["Да", "Нет"]

        elif key == "Тип недвижимости":
            return answer in ["Жилой", "Коммерческий", "Инвестиционный"]

        elif key == "Количество комнат":
            try:
                value = int(answer)
                return value > 0
            except ValueError:
                return False

        elif key == "Расположение":
            return answer in ["Октябрьский", "Ленинский", "Советский", "Кировский", "Пригород", ""]

        return True

    def check_and_transform_budget(self):
        # Проверяем корректность ввода бюджета и преобразуем из числового типа в категориальное
        try:
            budget_value = int(self.facts["Бюджет"])
        except ValueError:
            print("Ошибка преобразования бюджета в число")
            return False

        if budget_value < 1_000_000:
            if self.facts.get("Ипотека") == "Нет":
                return False
            else:
                self.facts["Бюджет"] = "Низкий"

        elif budget_value < 3_000_000:
            self.facts["Бюджет"] = "Низкий"

        elif budget_value < 5_000_000:
            self.facts["Бюджет"] = "Средний"

        else:
            self.facts["Бюджет"] = "Высокий"

        return True

    def print_facts(self):
        # Выводим ответы пользователя в терминал
        print("\nВаши ответы:")
        for key, value in self.facts.items():
            print(f"{key}: {value}")

    def get_recommendations(self):
        # Список для хранения рекомендаций в формате (вариант, нормированный балл, число условий)
        recs = []
        for rule in self.rules:
            conditions = rule.get("if", {})
            total = len(conditions)
            # Если условий нет, считаем балл равным 0, иначе вычисляем процент совпадения
            score = 0 if total == 0 else (sum(1 for k, v in conditions.items() if self.facts.get(k) == v) / total) * 100
            recs.append((rule["then"], score, total))
        
        # Сортируем сначала по нормированному баллу, затем по количеству условий (больше – лучше)
        recs.sort(key=lambda x: (x[1], x[2]), reverse=True)
        
        # Возвращаем только текст варианта и нормированный балл
        return [(text, score) for text, score, _ in recs]


    def predict(self):
        # Основной метод для запуска процесса: проверяем бюджет, выводим факты
        # Применяем правила и выводим наилучшие варианты
        if not self.check_and_transform_budget():
            print("Рекомендую увеличить бюджет.")
            return

        self.print_facts()
        recommendations = self.get_recommendations()

        print("\nРекомендованные варианты (от наилучшего к менее подходящему):")
        top_recommendations = [rec for rec in recommendations if rec[1] > 0][:3]

        if top_recommendations:
            for target, score in top_recommendations:
                print(f"Вариант: {target} | Балл: {score:.2f}")
        else:
            print("Нет подходящих вариантов. Попробуйте изменить условия.")
