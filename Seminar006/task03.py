# Задание №3

from functools import reduce


number = input('Введите вещественное число: ')
number = number.replace(',', '')
number = number.replace('.', '')
sumNum = reduce((lambda x, y: x + y), list(map(int, [el for el in number])))
print(f'Сумма всех цифр равна: {sumNum}')
