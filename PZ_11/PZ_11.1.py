"""1.В последовательности на n целых элементов найти количество пар, для которых
произведение элементов делится на 3 (элементы пары в последовательности являются
соседними)v."""
numbers = [2, 3, 6, 1, 9, 4, 7, 12, 5, 3]
pairs = list(zip(numbers, numbers[1:]))
print(f"Пары соседних элементов: {pairs}")

valid_pairs = list(filter(lambda pair: pair[0] * pair[1] % 3 == 0, pairs))

count = len(valid_pairs)

print(f"\nКоличество пар с произведением, кратным 3: {count}")
print(f"Найденные пары: {valid_pairs}")