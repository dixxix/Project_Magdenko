"""Приложение ЗАКАЗЫ ТОВАРОВ для автоматизированного контроля заказов
торговой фирмы. Таблица Заказы должна содержать информацию о товарах со следующей
структурой записи: Код товара, Наименование товара, Заказчик (наименование
организации, возможны повторяющиеся значения), Дата заказа, Срок исполнения (от 1 до
10 дней), Стоимость заказа."""
import sqlite3 as sq
import os
DB = "orders_v8.db"
def init_db():
    if os.path.exists(DB): os.remove(DB)
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE Orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            customer TEXT,
            date TEXT,
            term INTEGER CHECK(term BETWEEN 1 AND 10),
            cost REAL
        )""")
        data = [
            ("Ноутбук", "ООО Ромашка", "2026-05-01", 3, 50000),
            ("Мышь", "ИП Иванов", "2026-05-02", 1, 1500),
            ("Монитор", "ООО Ромашка", "2026-05-03", 5, 22000),
            ("Клавиатура", "ЗАО Вектор", "2026-05-04", 2, 3000),
            ("Принтер", "ИП Петров", "2026-05-05", 7, 12000),
            ("Кабель", "ООО Техно", "2026-05-06", 1, 500),
            ("Роутер", "ЗАО Вектор", "2026-05-07", 3, 4500),
            ("Флешка", "ИП Иванов", "2026-05-08", 1, 800),
            ("Камера", "ООО Техно", "2026-05-09", 4, 2100),
            ("Наушники", "ИП Сидоров", "2026-05-10", 2, 7500)
        ]
        cur.executemany("INSERT INTO Orders (name, customer, date, term, cost) VALUES (?,?,?,?,?)", data)
def search_by_customer():
    cust = input("Поиск по заказчику: ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Orders WHERE customer LIKE ?", (f"%{cust}%",))
        for row in cur: print(row)

def search_by_product():
    product = input("Поиск по товару: ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Orders WHERE name LIKE ?", (f"%{product}%",))
        for row in cur: print(row)

def search_by_date():
    date = input("Поиск по дате (ГГГГ-ММ-ДД): ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Orders WHERE date = ?", (date,))
        for row in cur: print(row)

def edit_cost():
    pid = int(input("ID товара: "))
    new_cost = float(input("Новая цена: "))
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("UPDATE Orders SET cost = ? WHERE id = ?", (new_cost, pid))
        print("Цена обновлена." if cur.rowcount else "Не найдено.")

def edit_term():
    pid = int(input("ID товара: "))
    new_term = int(input("Новый срок (1-10 дней): "))
    if 1 <= new_term <= 10:
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("UPDATE Orders SET term = ? WHERE id = ?", (new_term, pid))
            print("Срок обновлен." if cur.rowcount else "Не найдено.")
    else:
        print("Срок должен быть от 1 до 10 дней!")

def edit_customer():
    pid = int(input("ID товара: "))
    new_customer = input("Новый заказчик: ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("UPDATE Orders SET customer = ? WHERE id = ?", (new_customer, pid))
        print("Заказчик обновлен." if cur.rowcount else "Не найдено.")

def delete_by_term():
    term = int(input("Удалить заказы со сроком (дней): "))
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM Orders WHERE term = ?", (term,))
        print(f"Удалено записей: {cur.rowcount}")

def delete_by_id():
    pid = int(input("ID товара для удаления: "))
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM Orders WHERE id = ?", (pid,))
        print(f"Удалено записей: {cur.rowcount}")

def delete_by_customer():
    cust = input("Удалить заказы заказчика: ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM Orders WHERE customer = ?", (cust,))
        print(f"Удалено записей: {cur.rowcount}")
init_db()
while True:
    print("МЕНЮ ")
    print("1-Показать все заказы")
    print("2-Поиск по заказчику")
    print("3-Поиск по товару")
    print("4-Поиск по дате")
    print("5-Изменить цену")
    print("6-Изменить срок")
    print("7-Изменить заказчика")
    print("8-Удалить по сроку")
    print("9-Удалить по ID")
    print("10-Удалить по заказчику")
    print("0-Выход")

    cmd = input("Выберите:")
    if cmd == '1':
        with sq.connect(DB) as con:
            for row in con.cursor().execute("SELECT * FROM Orders"): print(row)
    elif cmd == '2':
        search_by_customer()
    elif cmd == '3':
        search_by_product()
    elif cmd == '4':
        search_by_date()
    elif cmd == '5':
        edit_cost()
    elif cmd == '6':
        edit_term()
    elif cmd == '7':
        edit_customer()
    elif cmd == '8':
        delete_by_term()
    elif cmd == '9':
        delete_by_id()
    elif cmd == '10':
        delete_by_customer()
    elif cmd == '0':
        break