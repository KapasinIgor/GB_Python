# Задание №1

userList = [2, 3, 5, 9, 3]
userSum = 0

for count, value in enumerate(userList):
    if count % 2:
        userSum += value

print(f'Сумма значений нечетных индексов равна: {userSum}')
