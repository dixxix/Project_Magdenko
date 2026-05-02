import random
try:
    rows = int(input("Количество строк: "))
    cols = int(input("Количество столбцов: "))
    matrix = [[random.randint(1, 20) for _ in range(cols)] for _ in range(rows)]
    print("Исходная матрица:")
    for row in matrix:
        print(' '.join(map(str, row)))
    result = list(map(lambda x, idx: [0] * len(x) if idx == len(matrix)-1 else x,
                      matrix, range(len(matrix))))
    print("Результат (последняя строка заменена на нули):")
    list(map(print, map(lambda x: ' '.join(map(str, x)), result)))
except ValueError:
    print("Ошибка: введите корректные числа")