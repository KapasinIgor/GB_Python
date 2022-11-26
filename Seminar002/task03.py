# Задача №3

n = int(input('Введите число последовательностей: '))
sumNum = 0

for i in range(1, n + 1):
    sumNum += round((1 + 1 / i) ** i, 2)

print(f'Результат: {sumNum}')
