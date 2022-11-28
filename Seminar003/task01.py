# Задача №1

userList = [2, 3, 5, 9, 3]
userSum = 0

for i in range(len(userList)):
    if i % 2:
        userSum += userList[i]

print(f'Сумма значений нечетных индексов равна: {userSum}')