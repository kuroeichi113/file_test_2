class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        self.save_to_file()

    def update_contact(self, name, new_number):
        if name in self.contacts:
            self.contacts[name] = new_number
            self.save_to_file()
            print(f"Контакт {name} успешно обновлен")
        else:
            print(f"Контакт {name} не найден")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_to_file()
            print(f"Контакт {name} успешно удален")
        else:
            print(f"Контакт {name} не найден")

    def display_contacts(self):
        if self.contacts:
            print("Телефонный справочник:")
            for name, number in self.contacts.items():
                print(f"{name}: {number}")
        else:
            print("Телефонный справочник пуст")

    def save_to_file(self):
        with open("phonebook.txt", "w") as file:
            for name, number in self.contacts.items():
                file.write(f"{name}: {number}\n")


def load_from_file():
    phone_book = PhoneBook()
    try:
        with open("phonebook.txt", "r") as file:
            for line in file:
                name, number = line.strip().split(": ")
                phone_book.add_contact(name, number)
    except FileNotFoundError:
        pass
    return phone_book


phone_book = load_from_file()

while True:
    print("\nВыберите действие:")
    print("1. Добавить контакт")
    print("2. Обновить контакт")
    print("3. Удалить контакт")
    print("4. Показать все контакты")
    print("5. Выйти")

    choice = input("Введите номер действия: ")

    if choice == "1":
        name = input("Введите имя контакта: ")
        number = input("Введите номер телефона: ")
        phone_book.add_contact(name, number)
    elif choice == "2":
        name = input("Введите имя контакта для обновления: ")
        new_number = input("Введите новый номер телефона: ")
        phone_book.update_contact(name, new_number)
    elif choice == "3":
        name = input("Введите имя контакта для удаления: ")
        phone_book.delete_contact(name)
    elif choice == "4":
        phone_book.display_contacts()
    elif choice == "5":
        print("Сохранение изменений и выход из программы...")
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")
