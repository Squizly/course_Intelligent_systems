from knowledge_base.questions import questions


if __name__ == "__main__":

    answers = {}

    for q in questions:
        answers[q["Ключ"]] = input(q["Значение"])
    
    for key, value in answers.items():
        print(f"{key} : {value}")