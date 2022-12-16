from data_action import *
from logger import status_log, clear_log
from database import clear_db
from export_html import create_html


def carousel_of_choice():
    cycle = "да"
    while cycle == "да":
        print("\nВыберите действие:\n\
        1 - Добавить контакт\n\
        2 - Вывести книгу на экран\n\
        3 - Найти контакт\n\
        4 - Экспорт книги в Html\n\
        5 - Очистить книгу и лог-файл")
        unit = input("Введите цифру: ")
        print(" ")
        action(unit)
        cycle = input("\nПродолжить работу? (Да/Нет): ").lower()


def action(unit):
    if unit == '1':
        inp_dt = input_data()
        add_data(inp_dt)
        status_log(f"Добавлен новый контакт - {' '.join(inp_dt)}")

    if unit == '2':
        data = output_data()
        print_data(data)
        status_log("Вывод книги на экран(консоль)")

    if unit == '3':
        word = input("Введите данные для поиска: ")
        data = output_data()
        item = search_data(word, data)
        if item is not None:
            print("Фамилия".center(15), "Имя".center(15), "Телефон".center(15))
            print("-" * 50)
            print(item[0].center(15), item[1].center(15), item[2].center(15))
        else:
            print("Данные не обнаружены")
        status_log(f"Поиск контакта - {' '.join(item)}")

    if unit == '4':
        create_html()
        status_log("Произведен экспорт книги в Html формат")

    if unit == '5':
        clear_db()
        clear_log()
        print("- База данных и лог-файл очищены\n")
