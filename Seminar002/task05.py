# Задача №5
import random

number = int(input('Введите длину списка: '))
userList = []

for i in range(number):
    userList.append(i)

print(f'Начальный список: {userList}')
random.shuffle(userList)
print(f'Перемешанный список: {userList}')
