# Задача №1

number = input('Введите вещественное число: ')
sumNum = 0
number = number.replace(',', '')
number = number.replace('.', '')
for el in number:
    sumNum += int(el)
print(f'Сумма всех цифр равна: {sumNum}')
