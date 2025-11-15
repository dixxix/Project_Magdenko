"""
Составить программу, в которой функция построит изображение, в котором в
первой строке 1 звездочка, во второй - 2, в третьей - 3, ..., в строке с номером m - m
звездочек
"""
def draw_stars(rows):
    print(f"Рисуем треугольник из {rows} строк:")
    i = 1
    while i <= rows:
        print('*' * i)
        i += 1
def main():
    try:
        user_input = input("Введите количество строк: ")
        number_of_rows = int(user_input)
        if number_of_rows > 0:
            draw_stars(number_of_rows)
        else:
            print("Ошибка: введите число больше 0!")
    except ValueError:
        print("Ошибка: нужно ввести целое число!")
main()