import json

# Читаем содержимое вашего текстового файла
input_file_path = "bd_text.txt"  # Замените на путь к вашему файлу
output_file_path = "knowledge_base.json"

with open(input_file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

knowledge_base = []
current_rule = {}

for line in lines:
    line = line.strip()
    if line.startswith("Условия для покупки недвижимости :"):
        if current_rule:  # Если есть собранное правило, добавляем его в список
            knowledge_base.append(current_rule)
            current_rule = {}
    elif "Необходимый бюджет :" in line:
        current_rule["budget"] = line.split(":")[1].strip()
    elif "Семейное положение :" in line:
        current_rule["marital_status"] = line.split(":")[1].strip()
    elif "Детей" in line:
        current_rule["children"] = line.split(":")[1].strip()
    elif "инфраструктура" in line:
        current_rule["infrastructure_priority"] = line.split(":")[1].strip()
    elif "Рекомендуется" in line:
        current_rule["recommendation"] = line.split("Рекомендуется")[1].strip()

# Добавляем последнее правило, если оно есть
if current_rule:
    knowledge_base.append(current_rule)

# Сохраняем результат в JSON файл
with open(output_file_path, "w", encoding="utf-8") as json_file:
    json.dump(knowledge_base, json_file, ensure_ascii=False, indent=4)

print(f"Данные успешно преобразованы и сохранены в {output_file_path}")