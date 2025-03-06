import re

from knowledge_base.questions import *
from knowledge_base.rules import *
from expert_system import *


expert_system = RealEstateExpert(questions, rules)

expert_system.get_facts()
expert_system.convert_budget_to_category_type()

facts = set(expert_system.facts.values())
print(facts)



if (expert_system.backward_chaining("Однокомнатная студия эконом-класса в спальном районе", facts)):
    print(" ---> достигнут")
