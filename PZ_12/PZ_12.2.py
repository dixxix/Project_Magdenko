"""В матрице элементы последней строки заменить на 0."""
matrix = [list(map(int, input(f"Строка {i+1}: ").split()))
          for i in range(int(input("Строк: ")))]

# Замена последней строки на нули
result = list(map(lambda x, idx: [0] * len(x) if idx == len(matrix)-1 else x,
                  matrix, range(len(matrix))))

print("Результат:")
list(map(print, map(lambda x: ' '.join(map(str, x)), result)))