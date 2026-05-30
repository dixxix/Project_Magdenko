"""ПЗ 3.1:
Даны два целых числа: А, В.
Проверить истинность высказывания:
«Каждое из чисел А и В нечетное»"""
import tkinter as tk
def check_odd_numbers():
    try:
        val_a = entry_a.get()
        val_b = entry_b.get()

        if not val_a or not val_b:
            label_result.config(text="Ошибка: Заполните оба поля!", fg="red")
            return
        a = int(val_a)
        b = int(val_b)
        is_a_odd = (a % 2 != 0)
        is_b_odd = (b % 2 != 0)
        result = is_a_odd and is_b_odd
        if result:
            label_result.config(text=f"ИСТИНА: Числа {a} и {b} нечетные.", fg="green")
        else:
            reason = []
            if not is_a_odd:
                reason.append(f"{a} четное")
            if not is_b_odd:
                reason.append(f"{b} четное")
            label_result.config(text=f"ЛОЖЬ: {', '.join(reason)}.", fg="red")
    except ValueError:
        label_result.config(text="Ошибка: Введите целые числа!", fg="red")
root = tk.Tk()
root.title("ПЗ №14, Задание 2 - Проверка нечетности")
root.geometry("350x250")
root.configure(bg="#f0f0f0")

header_label = tk.Label(root, text="Проверка высказывания:", font=("Arial", 12, "bold"), bg="#f0f0f0")
header_label.pack(pady=10)
statement_label = tk.Label(root, text="«Каждое из чисел А и В нечетное»", font=("Arial", 10), bg="#f0f0f0", fg="#555")
statement_label.pack(pady=(0, 15))
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(fill='x', padx=20)

tk.Label(input_frame, text="Число A:", font=("Arial", 11), bg="#f0f0f0").pack(side='left', padx=5)
entry_a = tk.Entry(input_frame, width=10, font=("Arial", 11), bd=1, relief='solid')
entry_a.pack(side='left', padx=5)

tk.Label(input_frame, text="Число B:", font=("Arial", 11), bg="#f0f0f0").pack(side='left', padx=(15, 5))
entry_b = tk.Entry(input_frame, width=10, font=("Arial", 11), bd=1, relief='solid')
entry_b.pack(side='left', padx=5)

btn_check = tk.Button(root, text="Проверить", command=check_odd_numbers,
                      font=("Arial", 11, "bold"), bg="#3498db", fg="white",
                      padx=20, pady=5, cursor="hand2")
btn_check.pack(pady=20)

label_result = tk.Label(root, text="Результат будет здесь...", font=("Arial", 11),
                        bg="#f0f0f0", wraplength=300, justify='center')
label_result.pack(pady=10)

btn_exit = tk.Button(root, text="Закрыть", command=root.destroy,
                     font=("Arial", 10), bg="#e74c3c", fg="white", padx=10, pady=5)
btn_exit.pack(pady=5)
root.mainloop()