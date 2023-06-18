# ; Задача №49. Решение в группах
# ; Создать телефонный справочник с
# ; возможностью импорта и экспорта данных в
# ; формате .txt. Фамилия, имя, отчество, номер
# ; телефона - данные, которые должны находиться
# ; в файле.
# ; 1. Программа должна выводить данные
# ; 2. Программа должна сохранять данные в
# ; текстовом файле
# ; 3. Пользователь может ввести одну из
# ; характеристик для поиска определенной
# ; записи(Например имя или фамилию
# ; человека)
# ; 4. Использование функций. Ваша программа
# ; не должна быть линейной

file_path = "file.txt"
import re

def show_all_records():
    with (open(file_path, 'r', encoding="utf-8")) as _data:
        for line in _data:
            phonebook_data = line.replace(";", " ")
            print(phonebook_data, end="")


def search_record(searching_data):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if searching_data.lower() in line.split(";")[0].lower():
                print(line, end="")


def add_contact(new_contact_fio, new_contact_number):

    with open("file.txt", "a", encoding="utf-8") as f:
        f.write("\n")
        f.write(new_contact_fio.replace(" "," "))
        f.write(' ')
        f.write(new_contact_number)


def record_name(contactOld, newName, newNumber):
    with open('file.txt', "r", encoding="utf-8") as f: 
        lines = f.readlines()
    pattern = re.compile(re.escape(contactOld))
    with open('file.txt', 'w', encoding="utf-8") as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
    with open("file.txt", "a", encoding="utf-8") as f:
        f.write("\n")
        f.write(newName.replace(" "," "))
        f.write(' ')
        f.write(newNumber)



def delite_contact(contact):
    with open('file.txt', "r", encoding="utf-8") as f: 
        lines = f.readlines()
    pattern = re.compile(re.escape(contact))
    with open('file.txt', 'w', encoding="utf-8") as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)


def main():
    print("Выберите действие: 1 - Показать справочник,"
          "2 - найти контакт,"
          "3 - добавить контакт" "4 - изменить контакт",
"5 - удалить контакт")
    select = int(input())
    if select == 1:
        show_all_records()
    elif select == 2:
        name = input("Введите фамилию: ")
        search_record(name)
    elif select == 3:
        fio = input("Введите ФИО через пробел: ")
        number = input("Введите Номер: ")
        add_contact(fio, number)
    elif select == 4:
        contactOld = input("Введите ФИО искомого контакта и телефон через пробел: ")
        newName = input("Введите измененные ФИО контакта: ")
        newNumber = input("Введите измененный номер контакта: ")
        record_name(contactOld, newName, newNumber)
    elif select == 5:
        contact = str(input("Введите ФИО и номер телефона через пробел: "))
        delite_contact(contact)
main()