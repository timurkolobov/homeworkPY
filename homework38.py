#Задача 38: Дополнить телефонный справочник возможностью изменения и 
#удаления данных. Пользователь также может ввести фамилию,
#и Вы должны реализовать функционал для изменения и удаления данных





def add_contact():
    surname = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")
    phonebook[surname] = phone
    print("Контакт успешно добавлен!")

def edit_contact():
    surname = input("Введите фамилию контакта, которого нужно изменить: ")
    if surname in phonebook:
        phone = input("Введите новый номер телефона: ")
        phonebook[surname] = phone
        print("Контакт успешно изменен!")
    else:
        print("Контакт с указанной фамилией не найден!")

def delete_contact():
    surname = input("Введите фамилию контакта, который нужно удалить: ")
    if surname in phonebook:
        del phonebook[surname]
        print("Контакт успешно удален!")
    else:
        print("Контакт с указанной фамилией не найден!")

def main():
    while True:
        print("Меню:")
        print("1. Добавить контакт")
        print("2. Изменить контакт")
        print("3. Удалить контакт")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()