# Задача №3

num_lst = []

for i in range(5):
    num_lst.append(int(input(f'Введите число {i}:')))

print("Уникальные цифры:", end=' ')

for i in num_lst:
    if num_lst.count(i) < 2:
        print(i, end=' ')
