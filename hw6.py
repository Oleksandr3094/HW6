from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
	pass

class Phone(Field):
    def __init__(self, value):
        phone_str = str(value)
        if not (phone_str.isdigit() and len(phone_str) == 10):
            raise ValueError("Номер телефону повинен складатися рівно з 10 цифр.")
        super().__init__(phone_str)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        found_phone = self.find_phone(phone)
        if found_phone:
            self.phones.remove(found_phone)

    def edit_phone(self, old_phone, new_phone):
        validated_phone = Phone(new_phone)  # Перевіряє new_phone на 10 цифр; при помилці кине ValueError
        found_phone = self.find_phone(old_phone)
        if found_phone:
            found_phone.value = validated_phone.value

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
          
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]



book = AddressBook()                  # 1. Створили порожню книгу (self.data == {})
john_record = Record("John")          # 2. Створили запис з name = Name("John") і phones = []
john_record.add_phone("1234567890")   # 3. Додали об'єкт Phone("1234567890") у john_record.phones
book.add_record(john_record)          # 4. Поклали весь Record у book.data["John"]

found = book.find("John")             # 5. Дістали об'єкт Record за рядком "John"
found.edit_phone("1234567890", "1112223333")  # 6. Змінили p.value всередині знайденого Record
print(found)                          # 7. Викликали Record.__str__
book.delete("John")                   # 8. Видалили запис "John" із book.data
