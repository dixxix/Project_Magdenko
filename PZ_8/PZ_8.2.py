"""2. Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16', отражающая
продажи продукции по дням в кг. Преобразовать информацию из строки в словари,
с использованием функции найти среднее значение продаж по каждому виду
продукции, результаты вывести на экран."""
string = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
parts = []
word = ''
for char in string:
    if char != ' ':
        word += char
    else:
        if word:
            parts.append(word)
            word = ''
if word:
    parts.append(word)
sales_dict = {}
current_fruit = ""
for item in parts:
    try:
        number = int(item)
        sales_dict[current_fruit].append(number)
    except ValueError:
        current_fruit = item
        sales_dict[current_fruit] = []
def get_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
print("Результаты:")
for fruit in sales_dict:
    avg = get_average(sales_dict[fruit])
    print(f"{fruit}: {avg:.1f} кг")