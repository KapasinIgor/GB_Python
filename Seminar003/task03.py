# Задача №3

userList: list[float | int] = [1.1, 1.2, 3.1, 5, 10.01]
maxNum: float | int = 0
minNum: float | int = userList[0]

for i in userList:
    if isinstance(i, float):
        if i % 1 > maxNum:
            maxNum = round(i % 1, 2)
        if i % 1 < minNum:
            minNum = round(i % 1, 2)

print(round(maxNum - minNum, 2))
