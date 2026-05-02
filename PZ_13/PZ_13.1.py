"""В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
Посчитать количество полученных элементов"""
import re
with open("Dostoevsky.txt", 'r', encoding='utf-8') as f:
    text = f.read()
pattern_str = r"Преступление и наказание|Идиот|Бесы|Братья Карамазовы|Подросток|Униженные и оскорблённые|Игрок|Записки из мертвого дома|Записки из подполья|Двойник|Бедные люди|Белые ночи"
p = re.compile(pattern_str)
found = p.findall(text)
unique_works = []
for work in found:
    if work not in unique_works:
        unique_works.append(work)
print(f"Найдено произведений: {len(unique_works)}")
for i, work in enumerate(unique_works, 1):
    print(f"{i}. {work}")