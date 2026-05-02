import random
try:
    rows = int(input("Количество строк: "))
    cols = int(input("Количество столбцов: "))
    n = int(input("Столбец (с 0): "))
    matrix = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]
    print("Исходная матрица:")
    for row in matrix:
        print(' '.join(map(str, row)))
    if not matrix:
        print("Матрица пуста")
    elif n < 0 or n >= len(matrix[0]):
        print(f"Ошибка: столбца {n} не существует. Всего столбцов: {len(matrix[0])}")
    else:
        result = list(map(lambda x: x[:n] + [x[n] * 2] + x[n + 1:], matrix))
        print("Результат (столбец", n, "увеличен в 2 раза):")
        list(map(print, map(lambda x: ' '.join(map(str, x)), result)))
except ValueError:
    print("Ошибка: введите корректные числа")