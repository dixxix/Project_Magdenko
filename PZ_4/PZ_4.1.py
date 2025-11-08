#Даны два целых числа А и В (А < В). Найти сумму квадратов всех целых чисел от А до В включительно.
try:
    A = int(input("Введите A: "))
    B = int(input("Введите B: "))

    if A >= B:
        print("Ошибка: A должно быть строго меньше B")
    else:
        summa = 0
        for i in range(A, B + 1):
            summa += i * i  # summa = summa + i * i
        print(f"Сумма квадратов чисел от {A} до {B} = {summa}")

except ValueError:
    print("Ошибка: Введите целые числа!")