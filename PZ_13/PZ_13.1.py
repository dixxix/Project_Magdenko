"""В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
Посчитать количество полученных элементов"""
import re

with open("Dostoevsky.txt", 'r', encoding='utf-8') as f:
    text = f.read()
pattern = r'[«"\']([^»"\']+)[»"\']'
p = re.compile(pattern)
found = p.findall(text)
unique_works = set(found)
print(f"Найдено произведений: {len(unique_works)}")
for i, work in enumerate(sorted(unique_works), 1):
    print(f"{i}. {work}")