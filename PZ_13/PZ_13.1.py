"""В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
Посчитать количество полученных элементов"""
import re
with open("Dostoevsky.txt", 'r', encoding='utf-8') as f:
    text = f.read()
works_patterns = [
    r'Преступление и наказание',
    r'Идиот',
    r'Бесы',
    r'Братья Карамазовы',
    r'Подросток',
    r'Униженные и оскорблённые',
    r'Игрок',
    r'Записки из мертвого дома',
    r'Записки из подполья',
    r'Двойник',
    r'Бедные люди',
    r'Белые ночи'
]
pattern_str = '|'.join([re.escape(w) for w in works_patterns])
p = re.compile(pattern_str)
found = p.findall(text)
unique_works = set(found)
print(f"Найдено произведений: {len(unique_works)}")
for i, work in enumerate(sorted(unique_works), 1):
    print(f"{i}. {work}")