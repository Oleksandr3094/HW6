from collections import UserDict, UserList, UserString

# class MyDictionary(UserDict):
#     # Приклад додавання нового методу
#     def add_key(self, key, value):
#         self.data[key] = value

# # Створення екземпляра власного класу
# my_dict = MyDictionary({'a': 1, 'b': 2})
# my_dict.add_key('c', 3)
# print(my_dict)

# contacts = [
#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False,
#     },
#     {
#         "name": "Chaim Lewis",
#         "email": "dui.in@egetlacus.ca",
#         "phone": "(294) 840-6685",
#         "favorite": False,
#     },
#     {
#         "name": "Kennedy Lane",
#         "email": "mattis.Cras@nonenimMauris.net",
#         "phone": "(542) 451-7038",
#         "favorite": True,
#     }
# ]

# class Customer(UserDict):
#     def phone_info(self):
#         return f"{self.get('name')}: {self.get('phone')}"

#     def email_info(self):
#         return f"{self.get('name')}: {self.get('email')}"


# if __name__ == "__main__":
#     customers = [Customer(el) for el in contacts]

#     print("---------------------------")

#     for customer in customers:
#         print(customer.phone_info())

#     print("---------------------------")

#     for customer in customers:
#         print(customer.email_info())


# class MyList(UserList):
#     # Додавання спеціалізованої поведінки. Наприклад, метод для додавання елемента, якщо він ще не існує
#     def add_if_not_exists(self, item):
#         if item not in self.data:
#             self.data.append(item)

# # Створення екземпляру MyList
# my_list = MyList([1, 2, 3])
# print("Оригінальний список:", my_list)

# # Додавання елементу, якщо він не існує
# my_list.add_if_not_exists(3)  # Не додасться, бо вже існує
# my_list.add_if_not_exists(4)  # Додасться, бо ще не існує
# print("Оновлений список:", my_list)


# class CountableList(UserList):
#     def sum(self):
#         return sum(map(lambda x: int(x), self.data))

# countable = CountableList([1, '2', 3, '4'])
# countable.append('5')
# print(countable.sum())


# # Створення класу, який розширює UserString
# class MyString(UserString):
#     # Додавання методу, який перевіряє, чи рядок є паліндромом
#     def is_palindrome(self):
#         return self.data == self.data[::-1]

# # Створення екземпляру MyString
# my_string = MyString("radar")
# print("Рядок:", my_string)
# print("Чи є паліндромом?", my_string.is_palindrome())

# # Створення іншого екземпляру MyString
# another_string = MyString("hello")
# print("Рядок:", another_string)
# print("Чи є паліндромом?", another_string.is_palindrome())


# class TruncatedString(UserString):
#     MAX_LEN = 7

#     def truncate(self):
#         self.data = self.data[:self.MAX_LEN]

# ts = TruncatedString('hello world!')
# ts.truncate()
# print(ts)


from dataclasses import dataclass

# @dataclass
# class ExampleClass:
#     attribute1: type
#     attribute2: type 

# @dataclass
# class Person:
#     name: str
#     age: int

# @dataclass
# class Article:
#     title: str
#     author: str
#     views: int = 0


# @dataclass
# class Rectangle:
#     width: int
#     height: int

#     def area(self) -> int:
#         return self.width * self.height

# rect1 = Rectangle(10, 5)
# rect2 = Rectangle(7, 3)
# rect3 = Rectangle(8, 6)

# print(f"Площа прямокутника 1: {rect1.area()}")
# print(f"Площа прямокутника 2: {rect2.area()}")
# print(f"Площа прямокутника 3: {rect3.area()}")

from enum import Enum, auto

# class Day(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7

# today = Day.MONDAY
# print(today)  # Виведе: Day.MONDAY
# if today == Day.MONDAY:
#     print("Сьогодні понеділок.")
# else:
#     print("Сьогодні не понеділок.")
# print(today.name)  
# print(today.value)  
# day_from_value = Day(1)
# print(day_from_value)  # Виведе: Day.MONDAY

# class OrderStatus(Enum):
#     NEW = auto()
#     PROCESSING = auto()
#     SHIPPED = auto()
#     DELIVERED = auto()

# class Order:
#     def __init__(self, name: str, status: OrderStatus):
#         self.name = name
#         self.status = status

#     def update_status(self, new_status: OrderStatus):
#         self.status = new_status
#         print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

#     def display_status(self):
#         print(f"Статус замовлення '{self.name}': {self.status.name}.")


# order1 = Order("Ноутбук", OrderStatus.NEW)
# order2 = Order("Книга", OrderStatus.NEW)

# order1.display_status()
# order2.display_status()

# order1.update_status(OrderStatus.PROCESSING)
# order2.update_status(OrderStatus.SHIPPED)

# order1.display_status()
# order2.display_status()


# Визначення власного класу винятку
class AgeVerificationError(Exception):
    def __init__(self, message="Вік не задовольняє мінімальній вимозі"):
        self.message = message
        super().__init__(self.message)

# Функція для перевірки віку
def verify_age(age: int):
    if age < 18:
        raise AgeVerificationError("Вік особи меньший за 18 років")

if __name__ == "__main__":
    # Обробка винятку
    try:
        verify_age(16)  # Змініть вік для різних результатів
    except AgeVerificationError as e:
        print(f"Виняток: {e}")
    else:
        print("Вік перевірено, особа доросла.")

class NameTooShortError(Exception):
    pass

class NameStartsFromLowError(Exception):
    pass

def enter_name():
    name = input("Enter name: ")
    if len(name) < 3:
        raise NameTooShortError("Name is too short, need more than 2 symbols")
    if not name[0].isupper():
        raise NameStartsFromLowError("Name should start from capital letter")
    return name

if __name__ == "__main__":
    try:
        name = enter_name()
        print(f"Hello, {name}")
    except (NameTooShortError, NameStartsFromLowError) as e:
        print(e)
