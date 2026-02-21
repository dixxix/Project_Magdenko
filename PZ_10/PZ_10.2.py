"""Из предложенного текстового файла (text18-8.txt) вывести на экран его содержимое,
количество символов, принадлежащих к группе букв. Сформировать новый файл, в
который поместить текст в стихотворной форме предварительно удалив букву «с» из
текста."""
with open('text18-8.txt', 'r', encoding='utf-8') as f:
    content = f.read()
print("Содержимое файла:")
print(content)
letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
letter_count = 0
for char in content:
    if char in letters:
        letter_count += 1
print(f"Количество символов, принадлежащих к группе букв: {letter_count}")
chars_to_remove = ['с', 'С']
modified_content = ''
for char in content:
    if char not in chars_to_remove:
        modified_content += char
with open('text18-8_modified.txt', 'w', encoding='utf-8') as f:
    f.write(modified_content)
print(f"Новый файл создан: text18-8_modified.txt")