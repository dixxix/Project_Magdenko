#Дано целое число N (>0) и символ C. Вывести строку длины N, которая состоит из
# символов C.
while True:
    try:
        N = int(input("Введите целое число N (>0): "))
        if N > 0:
            break
        else:
            print("Число должно быть больше 0!")
    except ValueError:
        print("Введите целое число!")
C = input("Введите символ C: ")
if len(C) > 1:
    C = C[0]
    print(f"Будет использован первый символ: '{C}'")
result = C * N
print(result)