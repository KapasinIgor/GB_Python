# Задача №2

n = int(input('Введите число: '))
i = 1
res = []
count = 1

while i <= n:
    for j in range(1, i + 1):
        count *= j
    res.append(count)
    count = 1
    i += 1

print(f'Результат: {res}', sep=',', end='')
