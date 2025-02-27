from knowledge_base.questions import *
from knowledge_base.rules import *
from expert_system import *

if __name__ == "__main__":
    system = RealEstateExpertSystem(questions, rules)
    system.get_facts()
    system.predict()
