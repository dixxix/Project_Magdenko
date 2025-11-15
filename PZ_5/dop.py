"""
1. Даны три целых числа. Определить у какого числа больше сумма цифр. Вывод
результата предусмотреть в основной программе. Расчет суммы цифр оформить в
функции.
"""
def sum_digits(n):
    total = 0
    number_str = str(n)
    i = 0
    while i < len(number_str):
        if number_str[i].isdigit():
            total += int(number_str[i])
        i += 1
    return total
def main():
    try:
        num1 = int(input("Первое число: "))
        num2 = int(input("Второе число: "))
        num3 = int(input("Третье число: "))
        s1 = sum_digits(num1)
        s2 = sum_digits(num2)
        s3 = sum_digits(num3)
        max_sum = max(s1, s2, s3)
        print(f"\nСуммы цифр: {s1}, {s2}, {s3}")
        if s1 == max_sum:
            print("У первого числа самая большая сумма цифр")
        if s2 == max_sum:
            print("У второго числа самая большая сумма цифр")
        if s3 == max_sum:
            print("У третьего числа самая большая сумма цифр")
    except ValueError:
        print("Ошибка: введите целые числа!")
main()
"""
2. Рассчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в 
функции.
"""
def calculate_perimeter(a, b):
    return 2 * (a + b)
def calculate_area(a, b):
    return a * b
def main():
    try:
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        if length > 0 and width > 0:
            p = calculate_perimeter(length, width)
            s = calculate_area(length, width)
            print(f"Периметр: {p}")
            print(f"Площадь: {s}")
        else:
            print("Ошибка: длина и ширина должны быть больше 0")
    except ValueError:
        print("Ошибка: введите числа!")
main()
"""
3. Написать программу, подсчитывающую количество цифр числа, используя для
этого функцию.
"""
def count_digits(n):
    count = 0
    number_str = str(n)
    i = 0
    while i < len(number_str):
        if number_str[i].isdigit():
            count += 1
        i += 1
    return count
def main():
    try:
        number = input("Введите число: ")
        digit_count = count_digits(number)
        print(f"В числе {number} содержится {digit_count} цифр")
    except Exception as e:
        print("Произошла ошибка")
main()