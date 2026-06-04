"""Создайте класс "Человек" с атрибутами "имя", "возраст" и "пол". Напишите метод,
который выводит информацию о человеке в формате "Имя: имя, Возраст: возраст,
Пол: пол"."""
class Human:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")
person1 = Human("Алексей", 25, "Мужской")
person1.display_info()
person2 = Human("Мария", 30, "Женский")
person2.display_info()