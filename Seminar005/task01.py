# Задание №1

my_string = "Я люблю абвДжаву иабв Питон!"

print(' '.join(list(filter(lambda i: "абв" not in i, my_string.split()))))
