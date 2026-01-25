"""
   Дан список размера N.
   Найти количество участков, на которых его элементы
   монотонно возрастают.
   """
def task2():
    try:
        numbers = [1, 3, 5, 2, 4, 6, 8, 1, 2, 3, 4]
        print("Исходный список:", numbers)
        count = 0
        in_sequence = False
        for i in range(1, len(numbers)):
            if numbers[i] > numbers[i - 1]:
                if not in_sequence:
                    count += 1
                    in_sequence = True
            else:
                in_sequence = False
        print(f"Количество монотонно возрастающих участков: {count}")
    except Exception as e:
        print(f"Ошибка: {e}")


task2()