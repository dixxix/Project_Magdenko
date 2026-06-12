"""
Описать функцию AddLeftDigit(D, K), добавляющую к целому положительному
числу K слева цифру D (D — входной параметр целого типа, лежащий в диапазоне
1-9, K — параметр целого типа, являющийся одновременно входным и выходным).
С помощью этой функции последовательно добавить к данному числу K слева
данные цифры D1 и D2, выводя результат каждого добавления.
"""
def AddLeftDigit(D, K):
    return int(str(D) + str(K))
def main():
    try:
        K = int(input("Введите целое положительное число K: "))
        D1 = int(input("Введите первую цифру D1 (1-9): "))
        D2 = int(input("Введите вторую цифру D2 (1-9): "))
        if K <= 0:
            print("Ошибка: K должно быть положительным числом")
        elif not (1 <= D1 <= 9) or not (1 <= D2 <= 9):
            print("Ошибка: D1 и D2 должны быть от 1 до 9")
        else:
            K = AddLeftDigit(D1, K)
            print(f"После добавления {D1}: {K}")
            K = AddLeftDigit(D2, K)
            print(f"После добавления {D2}: {K}")

    except ValueError:
        print("Ошибка: введите корректные целые числа")
main()

def sum_digits(N):
    total = 0
    while N > 0:
        total += N % 10
        N //= 10
    return total
user_input = input("Введите число: ")
N = int(user_input)
if N < 10:
    print("Число должно состоять минимум из 2 цифр")
else:
    result = sum_digits(N)
    print("Сумма цифр:", result)

N = int(input("Введите число: "))

def calculate():
    total = 0
    counter = 1
    while counter <= N:
        total += 1 / counter
        counter += 1
    return total
if N == 0:
    print("На 0 делить нельзя")
else:
    result = calculate()
    print(f"Ряд чисел: 1, 1/2, 1/3, ..., 1/{N}")
    print(f"Сумма чисел ряда: {result}")