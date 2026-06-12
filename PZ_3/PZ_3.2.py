#Единицы длины пронумерованы следующим образом: 1 — дециметр, 2 — километр. 3 — метр, 4 — миллиметр, 5 — сантиметр.
# Дан номер единицы длины (целое число в диапазоне 1-5) и длина отрезка в этих единицах (вещественное число).
# Найти длину отрезка в метрах.
try:
    unit = int(input("Единица (1-дм, 2-км, 3-м, 4-мм, 5-см): "))
    length = float(input("Длина: "))

    if unit == 1:
        print(f"{length} дм = {length / 10} м")
    elif unit == 2:
        print(f"{length} км = {length * 1000} м")
    elif unit == 3:
        print(f"{length} м = {length} м")
    elif unit == 4:
        print(f"{length} мм = {length / 1000} м")
    elif unit == 5:
        print(f"{length} см = {length / 100} м")
    else:
        print("Ошибка! Введите число от 1 до 5")

except ValueError:
    print("Ошибка ввода чисел!")