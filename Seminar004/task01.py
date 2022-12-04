# Задача №1
import math

num: str = input("Введите точность: ")
print(round(math.pi, len(num) - 2))
