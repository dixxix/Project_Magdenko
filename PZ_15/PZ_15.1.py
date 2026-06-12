"""Приложение ЗАКАЗЫ ТОВАРОВ для автоматизированного контроля заказов торговой фирмы.
Таблица Заказы должна содержать информацию о товарах со следующей структурой записи:
Код товара, Наименование товара, Заказчик (наименование организации, возможны повторяющиеся значения),
 Дата заказа, Срок исполнения (от 1 до 10 дней), Стоимость заказа."""
import sqlite3 as sq
import os
from data import DATA

DB = "orders_v8.db"

def init_db():
    if os.path.exists(DB):
        os.remove(DB)
    try:
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS Orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                customer TEXT,
                date TEXT,
                term INTEGER CHECK(term BETWEEN 1 AND 10),
                cost REAL
            )""")

            cur.executemany(
                "INSERT INTO Orders (name, customer, date, term, cost) VALUES (?, ?, ?, ?, ?)", DATA)
            print("База данных успешно создана и заполнена.")
    except sq.Error as e:
        print(f"Ошибка инициализации БД: {e}")

def show_all():
    try:
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Orders")
            rows = cur.fetchall()
            if not rows:
                print("Записей нет.")
            else:
                for row in rows:
                    print(row)
    except sq.Error as e:
        print(f"Ошибка чтения: {e}")

def search_by_customer():
    cust = input("Поиск по заказчику: ")
    try:
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Orders WHERE customer LIKE ?", (f"%{cust}%",))
            rows = cur.fetchall()
            if not rows:
                print("Ничего не найдено.")
            else:
                for row in rows:
                    print(row)
    except sq.Error as e:
        print(f"Ошибка поиска: {e}")

def search_by_product():
    product = input("Поиск по товару: ")
    try:
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Orders WHERE name LIKE ?", (f"%{product}%",))
            rows = cur.fetchall()
            if not rows:
                print("Ничего не найдено.")
            else:
                for row in rows:
                    print(row)
    except sq.Error as e:
        print(f"Ошибка поиска: {e}")

def search_by_date():
    date = input("Поиск по дате (ГГГГ-ММ-ДД): ")
    try:
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Orders WHERE date = ?", (date,))
            rows = cur.fetchall()
            if not rows:
                print("Ничего не найдено.")
            else:
                for row in rows:
                    print(row)
    except sq.Error as e:
        print(f"Ошибка поиска: {e}")

def edit_cost():
    try:
        pid = int(input("ID товара: "))
        new_cost = float(input("Новая цена: "))
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("UPDATE Orders SET cost = ? WHERE id = ?", (new_cost, pid))
            print("Цена обновлена." if cur.rowcount else "Не найдено.")
    except ValueError:
        print("Ошибка ввода данных.")
    except sq.Error as e:
        print(f"Ошибка обновления: {e}")

def edit_term():
    try:
        pid = int(input("ID товара: "))
        new_term = int(input("Новый срок (1-10 дней): "))
        if 1 <= new_term <= 10:
            with sq.connect(DB) as con:
                cur = con.cursor()
                cur.execute("UPDATE Orders SET term = ? WHERE id = ?", (new_term, pid))
                print("Срок обновлен." if cur.rowcount else "Не найдено.")
        else:
            print("Срок должен быть от 1 до 10 дней!")
    except ValueError:
        print("Ошибка ввода данных.")
    except sq.Error as e:
        print(f"Ошибка обновления: {e}")

def edit_customer():
    try:
        pid = int(input("ID товара: "))
        new_customer = input("Новый заказчик: ")
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("UPDATE Orders SET customer = ? WHERE id = ?", (new_customer, pid))
            print("Заказчик обновлен." if cur.rowcount else "Не найдено.")
    except ValueError:
        print("Ошибка ввода данных.")
    except sq.Error as e:
        print(f"Ошибка обновления: {e}")

def delete_by_term():
    try:
        term = int(input("Удалить заказы со сроком (дней): "))
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Orders WHERE term = ?", (term,))
            print(f"Удалено записей: {cur.rowcount}")
    except ValueError:
        print("Ошибка ввода данных.")
    except sq.Error as e:
        print(f"Ошибка удаления: {e}")

def delete_by_id():
    try:
        pid = int(input("ID товара для удаления: "))
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Orders WHERE id = ?", (pid,))
            print(f"Удалено записей: {cur.rowcount}")
    except ValueError:
        print("Ошибка ввода данных.")
    except sq.Error as e:
        print(f"Ошибка удаления: {e}")

def delete_by_customer():
    cust = input("Удалить заказы заказчика: ")
    try:
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Orders WHERE customer = ?", (cust,))
            print(f"Удалено записей: {cur.rowcount}")
    except sq.Error as e:
        print(f"Ошибка удаления: {e}")
init_db()

while True:
    print("МЕНЮ")
    print("1 - Показать все заказы")
    print("2 - Поиск по заказчику")
    print("3 - Поиск по товару")
    print("4 - Поиск по дате")
    print("5 - Изменить цену")
    print("6 - Изменить срок")
    print("7 - Изменить заказчика")
    print("8 - Удалить по сроку")
    print("9 - Удалить по ID")
    print("10 - Удалить по заказчику")
    print("0 - Выход")

    cmd = input("Выберите действие: ")
    if cmd == '1':
        show_all()
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
    else:
        print("Неверная команда.")