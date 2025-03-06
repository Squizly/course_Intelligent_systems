import re

from knowledge_base.questions import *
from knowledge_base.rules import *
from expert_system import *


expert_system = RealEstateExpert(questions, rules)

expert_system.get_facts()

# Прямой вывод результата со списком рекомендаций --->
expert_system.fit()


# Обратный вывод результата --->
for rule in rules:

    if (expert_system.backward_chaining(rule["Результат"])):
        print(f"Система рекомендует : {rule["Результат"]}")
