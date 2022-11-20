# Задача №1

numberWeek = int(input("Введите цифру дня недели: "))
if ((numberWeek == 6) or (numberWeek == 7)) and (numberWeek < 8):
    print("Выходной день!")
elif numberWeek > 7:
    print("Нет такого дня!!! Попробуйте заново.")
else:
    print("День - будний(((")
