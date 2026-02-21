"""Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Исходные данные:
Количество элементов:
Индекс последнего минимального элемента:
Сумма элементов больших 10 во второй половине:"""
import random
digit = []
for i in range(10):
    digit.append(random.randint(-20, 30))

stroka = ''
for chislo in digit:
    stroka = stroka + str(chislo) + ' '

l = [stroka]
f3 = open('data_3.txt', 'w')
f3.writelines(l)
f3.close()

f4 = open('data_4.txt', 'w')
f4.write('Исходные данные: ')
f4.write('\n')
f4.writelines(l)
f4.close()

f3 = open('data_3.txt')
k = f3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()

min_element = k[0]
for i in range(len(k)):
    if k[i] < min_element:
        min_element = k[i]

last_min_index = 0
for i in range(len(k)):
    if k[i] == min_element:
        last_min_index = i

seredina = len(k) // 2
summa = 0
for i in range(seredina, len(k)):
    if k[i] > 10:
        summa += k[i]
f4 = open('data_4.txt', 'a')
f4.write('\n')
print('Количество элементов: ', len(k), file=f4)
print('Индекс последнего минимального элемента: ', last_min_index, file=f4)
print('Сумма элементов больших 10 во второй половине: ', summa, file=f4)
f4.close()

print('Исходные данные:', k)
print('Количество элементов:', len(k))
print('Индекс последнего минимального элемента:', last_min_index)
print('Сумма элементов больших 10 во второй половине:', summa)