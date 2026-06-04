"""Создание базового класса "Животное" и его наследование для создания классов
"Собака" и "Кошка". В классе "Животное" будут общие методы, такие как "дышать"
и "питаться", а классы-наследники будут иметь свои уникальные методы и свойства,
такие как "гавкать" и "мурлыкать"."""
class Animal:
    def __init__(self, species: str, age: int):
        self.species = species
        self.age = age

    def breathe(self):
        print(f"{self.species} дышит.")

    def eat(self):
        print(f"{self.species} питается.")

class Dog(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(species="Собака", age=age)
        self.name = name

    def bark(self):
        print(f"{self.name}  громко гавкает: Гав-гав")


class Cat(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(species="Кошка", age=age)
        self.name = name

    def purr(self):
        print(f"{self.name} тихо мурлычет: Муррр Муррр")

dog1 = Dog(name="Бобик", age=4)
dog1.breathe()
dog1.eat()
dog1.bark()

cat1 = Cat(name="Мурка", age=2)
cat1.breathe()
cat1.eat()
cat1.purr()