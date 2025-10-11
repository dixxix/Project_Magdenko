print("Задача 1")
# Ввести 2 числа. Если их произведение отрицательно, умножить его на 8, в противном случае увеличить его в 1.5 раза.
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
product = num1 * num2

if product < 0:
    result = product * 8
    print(f"Произведение отрицательное: {product} × 8 = {result}")
else:
    result = product * 1.5
    print(f"Произведение неотрицательное: {product} × 1.5 = {result}")

print("Задача 2")
# Вести число. Если оно четное, разделить его на 4, если нечетное - умножить на 5.
num = int(input("Введите целое число: "))
if num % 2 == 0:
    result = num / 4
    print(f"Число четное: {num} ÷ 4 = {result}")
else:
    result = num * 5
    print(f"Число нечетное: {num} × 5 = {result}")

print(" Задача 3")
# Ввести двухзначное число. Если сумма цифр числа четная, то увеличить число на 2, в противном случае уменьшить на 2.
number = int(input("Введите двухзначное число: "))

if 10 <= number <= 99:
    digit1 = number // 10  
    digit2 = number % 10  
    digit_sum = digit1 + digit2
    
    if digit_sum % 2 == 0:
        result = number + 2
        print(f"Сумма цифр ({digit_sum}) четная: {number} + 2 = {result}")
    else:
        result = number - 2
        print(f"Сумма цифр ({digit_sum}) нечетная: {number} - 2 = {result}")
else:
    print("Ошибка: введите двухзначное число!")



print("Задача 4")
# Дано целое число. Если оно является положительным, то прибавить к нему 20, в противном случае вычесть из него 5.
num = int(input("Введите целое число: "))

if num > 0:
    result = num + 20
    print(f"Число положительное: {num} + 20 = {result}")
else:
    result = num - 5
    print(f"Число не положительное: {num} - 5 = {result}")

print("Задача 5")
# Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
sum_nums = num1 + num2

if sum_nums % 5 == 0:
    result = sum_nums + 14
    print(f"Сумма ({sum_nums}) кратна 5: {sum_nums} + 1 = {result}")
else:
    result = sum_nums - 2
    print(f"Сумма ({sum_nums}) не кратна 5: {sum_nums} - 2 = {result}")