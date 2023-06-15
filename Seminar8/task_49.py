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
        f.write(';')
        f.write(new_contact_number)

def record_name(nameOld, nameNew, newNumber):
    with open('file.txt', 'r') as f1, open('file.txt', 'w') as f2:
        lines = f1.readlines()
        for line in lines:
            line = line.strip()
            if line == nameOld:
                f2.write(nameNew)
            else:
                f2.write(line)
    
    
    # with open ('file.txt', 'r') as f:
    #      for line in f:
    #         if old_name.lower() in line.split(";")[0].lower():
    #             old_name = f.read()
    #             new_name = old_name.replace(nameOld, nameNew)
    # with open ('test.txt', 'w') as f:
    #     f.write(new_name)
    # # with open ('file.txt', 'r') as f:
    # #     old_name = f.read()
    # #     new_name = old_name.replace(nameOld, nameNew)
    # # with open ('test.txt', 'w') as f:
    # #     f.write(new_name)


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
        nameOld = input("Введите ФИО искомого контакта через пробел: ")
        nameNew = input("Введите измененные ФИО контакта: ")
        newNumber = input("Введите новый номер контакта: ")
        record_name(nameOld, nameNew, newNumber)
    elif select == 5:
        name = input("Введите ФИО через пробел: ")
        delite_name(name)
main()