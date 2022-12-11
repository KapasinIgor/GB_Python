# Задание №2

from random import randint
from sympy import symbols
from math import prod
import re

f_path: str = 'task04.txt'

max_val: int = 100
k = int(input('Введите натуральную степень k:'))
kfc: list = [randint(-max_val, max_val) for i in range(k)] + [randint(1, max_val)]
x = symbols('x')
manychlen: tuple = sum(map(prod, zip(kfc, [x**i for i in range(k+1)]))), '= 0'

braces = r'[\(\),\']'

with open(f_path, 'w') as f_manychlen:
    f_manychlen.write(re.sub(braces, '', str(manychlen)))
