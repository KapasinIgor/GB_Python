# Задача №5

import sympy

f_path_file1 = 'task05_1.txt'
f_path_file2 = 'task05_2.txt'
f_path_file3 = 'task05_3.txt'

with open(f_path_file1, 'r') as file_1:
    manychlen_1: str = file_1.read().replace('= 0', '+')

with open(f_path_file2, 'r') as file_2:
    manychlen_2: str = file_2.read().split('=')[0]

x = sympy.symbols('x')

manychlen_sum = sympy.powsimp(manychlen_1 + manychlen_2)

with open(f_path_file3, 'w') as file_3:
    file_3.writelines(f'{str(manychlen_sum)} = 0')
