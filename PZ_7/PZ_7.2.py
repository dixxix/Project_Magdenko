# Дана строка-предложение с избыточными пробелами между словами.
# Преобразовать ее так, чтобы между словами был ровно один пробел.
def remove_extra_spaces(text):
    try:
        if not isinstance(text, str):
            raise TypeError("Ожидалась строка")
        return ' '.join(text.split())
    except Exception as e:
        print(f"Ошибка: {e}")
        return ""
text = "  Дана    строка-предложение            с   избыточными                    пробелами               между   словами.  "
result = remove_extra_spaces(text)
print(f"Исходная: '{text}'")
print(f"Результат: '{result}'")