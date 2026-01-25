"""
Дан список размера N.
Заменить каждый элемент списка на среднее арифметическое
этого элемента и его соседей.
"""
def task3():
    try:
        numbers = [1, 4, 5 , 8, 10, 12]
        print("Исходный список:", numbers)
        result = numbers.copy()
        for i in range(len(numbers)):
            if i == 0:
                result[i] = (numbers[i] + numbers[i + 1]) / 2
            elif i == len(numbers) - 1:
                result[i] = (numbers[i - 1] + numbers[i]) / 2
            else:
                result[i] = (numbers[i - 1] + numbers[i] + numbers[i + 1]) / 3
        result = [round(x, 2) for x in result]
        print("Результат:", result)
    except Exception as e:
        print(f"Ошибка: {e}")
task3()