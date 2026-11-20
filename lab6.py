# class Person:
#     pass  # Порожній блок для тіла класу

# p = Person()

# class User:
#     name = 'Anonymous'
#     age = 15

# user1 = User()
# print(user1.name)
# print(user1.age)

# user2 = User()
# user2.name = "John"
# user2.age = 90

# print(user2.name)
# print(user2.age)

# class MyClass:
#     def __init__(self, value):
#         self.instance_field = value  # Поле класу

# obj1 = MyClass(5)
# obj2 = MyClass(10)


# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def say_name(self) -> None:
#         print(f'Hi! I am {self.name} and I am {self.age} years old.')

#     def set_age(self, age: int) -> None:
#         self.age = age

# bob = Person('Boris', 34)

# bob.say_name()
# bob.set_age(25)
# bob.say_name()


# class Person:
#     count = 0

#     def __init__(self, name: str):
#         self.name = name
#         Person.count += 1

#     def how_many_persons(self):
#         print(f"Кількість людей зараз {Person.count}")

# first = Person('Boris')
# first.how_many_persons()
# second = Person('Alex')
# first.how_many_persons()


# class Person:
#     count = 0

#     def __init__(self):
#         self.count = 10

# person = Person()
# print(person.count)  # 10
# print(Person.count)  # 0


# class Pokemon:
#     def __init__(self, name, type, health):
#         self.name = name
#         self.type = type
#         self.health = health

#     def attack(self, other_pokemon):
#         print(f"{self.name} attacks {other_pokemon.name}!")

#     def dodge(self):
#         print(f"{self.name} dodged the attack!")

#     def evolve(self, new_form):
#         print(f"{self.name} is evolving into {new_form}!")
#         self.name = new_form

# # Створення об'єкта Pikachu
# pikachu = Pokemon("Pikachu", "Electric", 100)

# # Використання методів
# pikachu.attack(Pokemon("Charmander", "Fire", 100))
# pikachu.dodge()
# pikachu.evolve("Raichu")

            
# Інкапсуляція - це концепція об'єктно-орієнтованого програмування, яка дозволяє 
# приховувати внутрішні деталі реалізації класу та надавати доступ до них лише через 
# визначені методи. Це допомагає захистити дані та забезпечити контроль над тим, як 
# вони використовуються.

# class Person:
#     def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
#         self.name = name
#         self.age = age
#         self._is_active = is_active
#         self.__is_admin = is_admin

#     def greeting(self):
#         return f"Hi {self.name}"

#     def is_active(self):
#         return self._is_active

#     def set_active(self, active: bool):
#         self._is_active = active

#     def get_is_admin(self):
#         return self.__is_admin

#     def set_is_admin(self, is_admin: bool):
#         # Тут можна додати будь-яку логіку перевірки або обробки
#         self.__is_admin = is_admin

        
# p = Person("Boris", 34, True, False)
# print(p.get_is_admin())
# p.set_is_admin(True)
# print(p.get_is_admin())


# Наслідування - це механізм об'єктно-орієнтованого програмування, який дозволяє 
# створювати нові класи на основі існуючих.


# class Animal:
#     def __init__(self, nickname: str, age: int):
#         self.nickname = nickname
#         self.age = age

#     def make_sound(self):
#         pass

# class Cat(Animal):
#     def make_sound(self) -> str:
#         return "Meow"

# class Dog(Animal):

#     def __init__(self, nickname: str, age: int, breed: str):
#         super().__init__(nickname, age)  # Викликаємо конструктор базового класу
#         self.breed = breed  # Додаємо нову властивість

#     def make_sound(self) -> str:
#         return "Woof"

#     def chase_tail(self) -> str:
#         return f"{self.nickname} is chasing its tail!"

# class Cow(Animal):
#     def make_sound(self):
#         return "Moo"

# my_cat = Cat("Simon", 4)
# my_cow = Cow("Bessie", 3)

# print(my_cat.make_sound())  # Виведе "Meow"
# print(my_cow.make_sound())  # Виведе "Moo"

# my_dog = Dog("Rex", 5, "Golden Retriever")
# print(my_dog.make_sound())  # Виведе "Woof"
# print(my_dog.chase_tail())  # Виведе "Rex is chasing its tail!"

# Багаторівне наслідування - це концепція об'єктно-орієнтованого програмування, яка дозволяє '
# 'класу успадковувати властивості та методи від більш ніж одного батьківського класу. '
# 'Це може бути корисним у випадках, коли потрібно об'єднати функціональність з різних класів.

# class Animal:
#     def __init__(self, nickname: str, age: int):
#         self.nickname = nickname
#         self.age = age

#     def make_sound(self):
#         pass

# class Bird(Animal):
#     def make_sound(self):
#         return "Chirp"

# class Parrot(Bird):
#     def can_fly(self):
#         return True

# class TalkingParrot(Parrot):
#     def say_phrase(self, phrase):
#         return f"The parrot says: '{phrase}'"

# my_parrot = TalkingParrot("Alice", 2)
# print(my_parrot.make_sound())
# print(my_parrot.can_fly())
# print(my_parrot.say_phrase("Hello, World!"))


# Поліморфізм - це концепція об'єктно-орієнтованого програмування, яка дозволяє об'єктам 
# різних класів реагувати на однакові методи по-різному. Це забезпечує гнучкість та 
# розширюваність коду.
# Качина типізація - це концепція, яка дозволяє об'єктам різних класів використовувати '
# 'однакові методи або інтерфейси, якщо вони мають однакову поведінку. Це означає, що '
# 'якщо об'єкт "виглядає" як певний тип (має потрібні методи), то його можна використовувати 
# як цей тип, навіть якщо він не є його підкласом.

# class Animal:
#     def __init__(self, nickname: str, age: int):
#         self.nickname = nickname
#         self.age = age

#     def make_sound(self):
#         pass

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow"

# class Dog(Animal):
#     def make_sound(self):
#         return "Woof"

# def animal_sounds(animals):
#     for animal in animals:
#         print(animal.make_sound())

# animals = [Cat("Simon", 4), Dog("Rex", 5)]
# animal_sounds(animals)


# class Duck:
#     def quack(self):
#         print("Quack, quack!")

# class Person:
#     def quack(self):
#         print("I'm Quacking Like a Duck!")

# def make_it_quack(duck):
#     duck.quack()

# duck = Duck()
# person = Person()

# make_it_quack(duck)
# make_it_quack(person)


from typing import Protocol

class Speaker(Protocol):
    def speak(self) -> str:
        pass

class Dog:
    def speak(self) -> str:
        return "Woof"

class Cat:
    def speak(self) -> str:
        return "Meow"

class Robot:
    def speak(self) -> str:
        return "Beep boop"

def make_it_speak(speaker: Speaker) -> None:
    print(speaker.speak())

dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop
