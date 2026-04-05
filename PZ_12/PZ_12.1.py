"""В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза."""
try:
    matrix = [list(map(int, input(f"Строка {i + 1}: ").split()))
              for i in range(int(input("Строк: ")))]
    n = int(input("Столбец (с 0): "))
    if not matrix:
        print("Матрица пуста")
    elif n < 0 or n >= len(matrix[0]):
        print(f"Ошибка: столбца {n} не существует. Всего столбцов: {len(matrix[0])}")
    else:
        result = list(map(lambda x: x[:n] + [x[n] * 2] + x[n + 1:], matrix))
        print("Результат:")
        list(map(print, map(lambda x: ' '.join(map(str, x)), result)))
except ValueError:
    print("Ошибка: введите корректные числа")