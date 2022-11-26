# Задача №4

numberList = int(input('Введите число для создания списка: '))
elementsList = input('Введите позиции элементов через пробел : ')
userList = []
result = 1

elementsList = elementsList.split(" ")

for i in range(-numberList, numberList + 1):
    userList.append(i)

for j in elementsList:
    result *= userList[int(j)]

print(f'Результат: {result}')
