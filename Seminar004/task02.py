# Задача №2

num = int(input("Введите число: "))
i: int = 2
num_set = set([])
while i <= num:
    if num % i == 0:
        num_set.add(i)
        num //= i
        i = 2
    else:
        i += 1

print(f'Простые множители: {num_set}')
