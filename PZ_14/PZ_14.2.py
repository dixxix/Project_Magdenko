#ПЗ 9
import tkinter as tk
from tkinter import ttk

def solve_shop_task_gui():
    shops = {
        "Магнит": {"молоко", "соль", "сахар"},
        "Пятерочка": {"мясо", "молоко", "сыр"},
        "Перекресток": {"молоко", "творог", "сыр", "сахар"}
    }

    def calculate_results():
        text_result.delete(1.0, tk.END)

        try:
            no_cheese = []
            for shop_name, items in shops.items():
                if "сыр" not in items:
                    no_cheese.append(shop_name)

            milk_and_sugar = []
            for shop_name, items in shops.items():
                if "молоко" in items and "сахар" in items:
                    milk_and_sugar.append(shop_name)

            has_salt = []
            for shop_name, items in shops.items():
                if "соль" in items:
                    has_salt.append(shop_name)

            result_str = ""

            result_str += "1. Магазины, где НЕЛЬЗЯ купить сыр:\n"
            if no_cheese:
                result_str += f"   {', '.join(no_cheese)}\n"
            else:
                result_str += "   Нет таких магазинов\n"
            result_str += "\n"

            result_str += "2. Магазины, где есть МОЛОКО и САХАР:\n"
            if milk_and_sugar:
                result_str += f"   {', '.join(milk_and_sugar)}\n"
            else:
                result_str += "   Нет таких магазинов\n"
            result_str += "\n"

            result_str += "3. Магазины, где есть СОЛЬ:\n"
            if has_salt:
                result_str += f"   {', '.join(has_salt)}\n"
            else:
                result_str += "   Нет таких магазинов\n"

            text_result.insert(tk.END, result_str)

        except Exception as e:
            text_result.insert(tk.END, f"Ошибка при расчете: {e}")

    root = tk.Tk()
    root.title("ПЗ №14, Задание 2 - Вариант 8")
    root.geometry("500x400")
    root.configure(bg="#9ab8ff")

    header_label = tk.Label(root, text="Анализ ассортимента магазинов", font=("Arial", 14, "bold"), bg="#f0f0f0")
    header_label.pack(pady=10)

    data_frame = tk.LabelFrame(root, text="Исходные данные", font=("Arial", 10), bg="#f0f0f0", padx=10, pady=5)
    data_frame.pack(fill='x', padx=10, pady=5)

    data_text = "Магнит: молоко, соль, сахар\nПятерочка: мясо, молоко, сыр\nПерекресток: молоко, творог, сыр, сахар"
    tk.Label(data_frame, text=data_text, justify='left', bg="#f0f0f0").pack(anchor='w')

    btn_calc = tk.Button(root, text="Рассчитать", command=calculate_results, font=("Arial", 12, "bold"),
                         bg="#3498db", fg="white", padx=20, pady=5, cursor="hand2")
    btn_calc.pack(pady=10)

    result_label = tk.Label(root, text="Результаты:", font=("Arial", 11, "bold"), bg="#f0f0f0", anchor='w')
    result_label.pack(fill='x', padx=10, pady=(0, 5))

    text_result = tk.Text(root, height=10, width=50, font=("Arial", 11), wrap = tk.WORD, bd=2, relief='solid')
    text_result.pack(fill='both', expand=True, padx=10, pady=(0, 10))

    btn_exit = tk.Button(root, text="Закрыть", command=root.destroy, font=("Arial", 10), bg="#e74c3c", fg="white",
                         padx=10, pady=5)
    btn_exit.pack(pady=5)

    root.mainloop()


solve_shop_task_gui()