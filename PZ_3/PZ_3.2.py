try:
    unit = int(input("Единица (1-дм, 2-км, 3-м, 4-мм, 5-см): "))
    length = float(input("Введите длинну отрезка: "))

    factors = [0.1, 1000, 1, 0.001, 0.01]
    names = ["дециметр", "километр", "метр", "миллиметр", "сантиметр"]

    if 1 <= unit <= 5:
        meters = length * factors[unit - 1]
        print(f"{length} {names[unit - 1]} = {meters} м")
    else:
        print("Ошибка диапазона!")

except ValueError:
    print("Ошибка ввода!")