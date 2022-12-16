
from database import path


def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите телефон: ")
    return [last_name, first_name, phone_number]


def print_data(data):
    if len(data) > 0:
        print("Фамилия".center(15), "Имя".center(15), "Телефон".center(15))
        print("-"*50)
        for item in data:
            print(item[0].center(15), item[1].center(15), item[2].center(15))
    else:
        print("В телефонном справочнике нет записей!")


def search_data(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None


def output_data():
    with open(path, 'r') as file:
        data = []
        for line in file:
            temp = line.strip().split(' ')
            data.append(temp)
    return data


def add_data(data):
    with open(path, 'a+') as file:
        file.write(' '.join(data))
        file.write(f"\n")
