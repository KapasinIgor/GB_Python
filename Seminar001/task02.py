# Задача №2

for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            a = (not (x or y or z)) == ((not (x)) and not (y) and not (z))
            print(f'¬({x} ⋁ {y} ⋁ {z}) = (¬{x} ⋀ ¬{y} ⋀ ¬{z})')
